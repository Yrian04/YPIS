from __future__ import annotations

from typing import Optional, cast

from antlr4 import ParserRuleContext
from antlr4.tree.Tree import TerminalNodeImpl as TerminalNode
from antlr4.tree.Tree import RuleNode

from toylang.generated.ToyLangParser import ToyLangParser
from toylang.generated.ToyLangParserListener import ToyLangParserListener
import toylang.operators as toy_operators
import toylang.types as toy_types


type Func = toy_types.FuncType_


class SemanticError:
    def __init__(self, line: int, col: int, msg: str):
        self.line = line
        self.col = col
        self.msg = msg

    def __str__(self):
        return f"Line {self.line}:{self.col}: {self.msg}"


set_ops = {
    '+': toy_operators.union,
    '*': toy_operators.intersection,
    '\\': toy_operators.difference,
    '@': toy_operators.product,
}

element_ops = {
    'in': toy_operators.in_,
}

comp_ops = {
    'eq': toy_operators.eq_,
    'ne': toy_operators.ne_,
    'gt': toy_operators.gt_,
    'lt': toy_operators.lt_,
    'ge': toy_operators.ge_,
    'le': toy_operators.le_,
}

cond_ops = {
    **element_ops,
    **comp_ops,
}

logical_ops = {
    'and': toy_operators.and_,
    'or': toy_operators.or_,
}

bin_ops: dict[str, toy_operators.Operator] = {
    **set_ops,
    **element_ops,
    **cond_ops,
    **logical_ops,
}

unary_ops = {
    'not': toy_operators.not_,
}

class SymbolTable:
    def __init__(self, parent: Optional[SymbolTable] = None):
        self.funcs: dict[str, toy_types.Type_] = {}
        self.parent = parent
    
    def define(self, name: str, symbol: toy_types.Type_):
        self.funcs[name] = symbol

    def lookup(self, id: str) -> toy_types.Type_:
        if id in self.funcs:
            return self.funcs[id]
        if self.parent:
            return self.parent.lookup(id)
        return toy_types.element_
        

class Namespace:
    def __init__(self):
        self.symbol_table: Optional[SymbolTable] = None
    
    def __getitem__(self, id: str) -> toy_types.Type_:
        return self.get_symbol(id)
    
    def __setitem__(self, id: str, symbol: toy_types.Type_) -> None:
        self.set_symbol(id, symbol)
    
    def get_symbol(self, id: str) -> toy_types.Type_:
        if self.symbol_table is None:
            raise RuntimeError('No symbol table')
        return self.symbol_table.lookup(id)
    
    def set_symbol(self, name: str, symbol: toy_types.Type_):
        if self.symbol_table is None:
            raise RuntimeError('No symbol table')
        self.symbol_table.define(name, symbol)

    def enter_scope(self) -> None:
        self.symbol_table = SymbolTable(parent=self.symbol_table)

    def exit_scope(self) -> None:
        if self.symbol_table is None:
            raise RuntimeError('No symbol table')
        self.symbol_table = self.symbol_table.parent


class SemanticAnalyzer(ToyLangParserListener):
    def __init__(self):
        self.ns = Namespace()
        self.errors: list[SemanticError] = []

    def add_error(self, ctx: TerminalNode | RuleNode, message):
        token = (
            ctx.getSymbol() 
            if isinstance(ctx, TerminalNode) 
            else ctx.start # type: ignore
        )
        line = token.line
        column = token.column
        self.errors.append(SemanticError(line, column, message))
        
    def get_expr_type(
        self, 
        ctx: ToyLangParser.ExprContext,
    ) -> toy_types.Type_:
        op = None
        in_args = None
        if ctx.atom():
            atom = cast(ToyLangParser.AtomContext, ctx.atom())
            if atom.literal():
                lit = cast(ToyLangParser.LiteralContext, atom.literal())
                if lit.bool_():
                    return toy_types.bool_
                if lit.set_():
                    return toy_types.set_
            elif atom.ID():
                id_node = cast(TerminalNode, atom.ID())
                return self.ns[id_node.getText()]
        elif ctx.LPAREN and ctx.RPAREN:
            return self.get_expr_type(ctx.expr()[0])
        elif (op:=cast(ParserRuleContext, ctx.unaryOperator())):
            inner_type = self.get_expr_type(ctx.expr(0))
            in_args = [inner_type]
            op = unary_ops[op.getText()]
        elif (op:=cast(
                ParserRuleContext,
                ctx.setOperator()
                or ctx.conditionalOperator()
                or ctx.logicalOperator()
            )
        ):
            left_type = self.get_expr_type(ctx.expr(0))
            right_type = self.get_expr_type(ctx.expr(1))
            in_args = [left_type, right_type]
            op = bin_ops[op.getText()]
        if op is not None and in_args is not None:
            try:
                return op.apply(in_args)
            except ValueError as e:
                self.add_error(ctx, e.args[0])
                return toy_types.unknown_
        self.add_error(ctx, 'Неизвестный оператор')
        return toy_types.unknown_
    
    def enterProgram(self, ctx: ToyLangParser.ProgramContext):
        self.ns.enter_scope()

    def exitProgram(self, ctx: ToyLangParser.ProgramContext):
        self.ns.exit_scope()

    def exitIf_(self, ctx: ToyLangParser.If_Context):
        cond_type = self.get_expr_type(ctx.expr(0))
        if cond_type not in (toy_types.bool_, toy_types.any_):
            self.add_error(
                ctx, 
                f"Условие 'if' должно быть булевым, "
                f"а не '{cond_type.name}'"
            )

    def exitWhile_(self, ctx: ToyLangParser.While_Context):
        cond_type = self.get_expr_type(ctx.expr())
        if cond_type not in (toy_types.bool_, toy_types.any_):
            self.add_error(
                ctx, 
                f"Условие 'while' должно быть булевым, "
                f"а не '{cond_type.name}'"
            )
    
    def enterFor_(self, ctx: ToyLangParser.For_Context):
        self.ns[ctx.ID()] = toy_types.any_

    def exitFor_(self, ctx: ToyLangParser.For_Context):
        iterable_type = self.get_expr_type(ctx.expr()) 
        if iterable_type not in (toy_types.set_, toy_types.any_):
            self.add_error(
                ctx, 
                f"Выражение 'For' должно быть булевым, "
                f"а не '{iterable_type.name}'"
            )
    
    def enterSubprogram(self, ctx: ToyLangParser.SubprogramContext):
        name: str = ctx.ID().getText()
        in_params_ctx = cast(
            Optional[ToyLangParser.In_paramsContext],
            ctx.in_params()
        )
        in_params_names: list[str] = [
            str(arg.getText()) 
            for arg in (in_params_ctx.ID() if in_params_ctx is not None else [])
        ]
        out_params_ctx = cast(
            Optional[ToyLangParser.Out_paramsContext],
            ctx.out_params()
        )
        out_params_names: list[str] = [
            str(arg.getText())
            for arg in (out_params_ctx.ID() if out_params_ctx is not None else [])
        ]
        self.ns[name] = toy_types.FuncType_(
            [toy_types.any_ for _ in in_params_names], 
            [toy_types.any_ for _ in out_params_names]
        )
        self.ns.enter_scope()
        for arg_name in in_params_names + out_params_names:
            self.ns[arg_name] = toy_types.any_

    def exitSubprogram(self, ctx: ToyLangParser.SubprogramContext):
        self.ns.exit_scope()

    def exitCall(self, ctx: ToyLangParser.CallContext):
        ids_ctxes = cast(list[TerminalNode], ctx.ID())
        func_name_ctx = ids_ctxes[0]
        func_name = str(func_name_ctx.getText())
        func = self.ns[func_name]
        if not isinstance(func, toy_types.FuncType_):
            self.add_error(func_name_ctx, f'{func_name} не подпрограмма')
            return
        in_args_types = [
            self.get_expr_type(expr_ctx) 
            for expr_ctx in ctx.expr()
        ]
        out_args_names = [
            str(arg_ctx.getText()) 
            for arg_ctx in ids_ctxes[1:]
        ] if len(ids_ctxes) > 1 else []
        try:
            out_args_types = func.apply(in_args_types)
        except ValueError as e:
            self.add_error(ctx, e.args[0])
            return
        if len(out_args_names) != len(out_args_types):
            self.add_error(
                ctx, 
                f'Подпрограмма {func_name} принимает {len(out_args_types)} '
                f'выходных аргумента, но было дано {len(out_args_names)}'
            )
            return
        for i, (name, type) in enumerate(zip(out_args_names, out_args_types)):
            if self.ns[name] is toy_types.element_:
                self.add_error(
                    ids_ctxes[i+1], 
                    f'Переменная {name} не объявлена'
                )
            else:
                self.ns[name] = type
    
    def exitAssignment(self, ctx: ToyLangParser.AssignmentContext):
        name = str(ctx.ID().getText())
        toy_type = self.get_expr_type(ctx.expr())
        self.ns[name] = toy_type
    