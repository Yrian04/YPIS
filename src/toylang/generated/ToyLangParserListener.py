# Generated from ToyLangParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ToyLangParser import ToyLangParser
else:
    from ToyLangParser import ToyLangParser

# This class defines a complete listener for a parse tree produced by ToyLangParser.
class ToyLangParserListener(ParseTreeListener):

    # Enter a parse tree produced by ToyLangParser#program.
    def enterProgram(self, ctx:ToyLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by ToyLangParser#program.
    def exitProgram(self, ctx:ToyLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by ToyLangParser#vars.
    def enterVars(self, ctx:ToyLangParser.VarsContext):
        pass

    # Exit a parse tree produced by ToyLangParser#vars.
    def exitVars(self, ctx:ToyLangParser.VarsContext):
        pass


    # Enter a parse tree produced by ToyLangParser#subprograms.
    def enterSubprograms(self, ctx:ToyLangParser.SubprogramsContext):
        pass

    # Exit a parse tree produced by ToyLangParser#subprograms.
    def exitSubprograms(self, ctx:ToyLangParser.SubprogramsContext):
        pass


    # Enter a parse tree produced by ToyLangParser#body.
    def enterBody(self, ctx:ToyLangParser.BodyContext):
        pass

    # Exit a parse tree produced by ToyLangParser#body.
    def exitBody(self, ctx:ToyLangParser.BodyContext):
        pass


    # Enter a parse tree produced by ToyLangParser#subprogram.
    def enterSubprogram(self, ctx:ToyLangParser.SubprogramContext):
        pass

    # Exit a parse tree produced by ToyLangParser#subprogram.
    def exitSubprogram(self, ctx:ToyLangParser.SubprogramContext):
        pass


    # Enter a parse tree produced by ToyLangParser#statement.
    def enterStatement(self, ctx:ToyLangParser.StatementContext):
        pass

    # Exit a parse tree produced by ToyLangParser#statement.
    def exitStatement(self, ctx:ToyLangParser.StatementContext):
        pass


    # Enter a parse tree produced by ToyLangParser#simple_statement.
    def enterSimple_statement(self, ctx:ToyLangParser.Simple_statementContext):
        pass

    # Exit a parse tree produced by ToyLangParser#simple_statement.
    def exitSimple_statement(self, ctx:ToyLangParser.Simple_statementContext):
        pass


    # Enter a parse tree produced by ToyLangParser#assignment.
    def enterAssignment(self, ctx:ToyLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ToyLangParser#assignment.
    def exitAssignment(self, ctx:ToyLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by ToyLangParser#call.
    def enterCall(self, ctx:ToyLangParser.CallContext):
        pass

    # Exit a parse tree produced by ToyLangParser#call.
    def exitCall(self, ctx:ToyLangParser.CallContext):
        pass


    # Enter a parse tree produced by ToyLangParser#compound_statement.
    def enterCompound_statement(self, ctx:ToyLangParser.Compound_statementContext):
        pass

    # Exit a parse tree produced by ToyLangParser#compound_statement.
    def exitCompound_statement(self, ctx:ToyLangParser.Compound_statementContext):
        pass


    # Enter a parse tree produced by ToyLangParser#if_.
    def enterIf_(self, ctx:ToyLangParser.If_Context):
        pass

    # Exit a parse tree produced by ToyLangParser#if_.
    def exitIf_(self, ctx:ToyLangParser.If_Context):
        pass


    # Enter a parse tree produced by ToyLangParser#for_.
    def enterFor_(self, ctx:ToyLangParser.For_Context):
        pass

    # Exit a parse tree produced by ToyLangParser#for_.
    def exitFor_(self, ctx:ToyLangParser.For_Context):
        pass


    # Enter a parse tree produced by ToyLangParser#while_.
    def enterWhile_(self, ctx:ToyLangParser.While_Context):
        pass

    # Exit a parse tree produced by ToyLangParser#while_.
    def exitWhile_(self, ctx:ToyLangParser.While_Context):
        pass


    # Enter a parse tree produced by ToyLangParser#until_.
    def enterUntil_(self, ctx:ToyLangParser.Until_Context):
        pass

    # Exit a parse tree produced by ToyLangParser#until_.
    def exitUntil_(self, ctx:ToyLangParser.Until_Context):
        pass


    # Enter a parse tree produced by ToyLangParser#block.
    def enterBlock(self, ctx:ToyLangParser.BlockContext):
        pass

    # Exit a parse tree produced by ToyLangParser#block.
    def exitBlock(self, ctx:ToyLangParser.BlockContext):
        pass


    # Enter a parse tree produced by ToyLangParser#expr.
    def enterExpr(self, ctx:ToyLangParser.ExprContext):
        pass

    # Exit a parse tree produced by ToyLangParser#expr.
    def exitExpr(self, ctx:ToyLangParser.ExprContext):
        pass


    # Enter a parse tree produced by ToyLangParser#atom.
    def enterAtom(self, ctx:ToyLangParser.AtomContext):
        pass

    # Exit a parse tree produced by ToyLangParser#atom.
    def exitAtom(self, ctx:ToyLangParser.AtomContext):
        pass


    # Enter a parse tree produced by ToyLangParser#literal.
    def enterLiteral(self, ctx:ToyLangParser.LiteralContext):
        pass

    # Exit a parse tree produced by ToyLangParser#literal.
    def exitLiteral(self, ctx:ToyLangParser.LiteralContext):
        pass


    # Enter a parse tree produced by ToyLangParser#set_.
    def enterSet_(self, ctx:ToyLangParser.Set_Context):
        pass

    # Exit a parse tree produced by ToyLangParser#set_.
    def exitSet_(self, ctx:ToyLangParser.Set_Context):
        pass


    # Enter a parse tree produced by ToyLangParser#in_params.
    def enterIn_params(self, ctx:ToyLangParser.In_paramsContext):
        pass

    # Exit a parse tree produced by ToyLangParser#in_params.
    def exitIn_params(self, ctx:ToyLangParser.In_paramsContext):
        pass


    # Enter a parse tree produced by ToyLangParser#out_params.
    def enterOut_params(self, ctx:ToyLangParser.Out_paramsContext):
        pass

    # Exit a parse tree produced by ToyLangParser#out_params.
    def exitOut_params(self, ctx:ToyLangParser.Out_paramsContext):
        pass


    # Enter a parse tree produced by ToyLangParser#bool_.
    def enterBool_(self, ctx:ToyLangParser.Bool_Context):
        pass

    # Exit a parse tree produced by ToyLangParser#bool_.
    def exitBool_(self, ctx:ToyLangParser.Bool_Context):
        pass


    # Enter a parse tree produced by ToyLangParser#setOperator.
    def enterSetOperator(self, ctx:ToyLangParser.SetOperatorContext):
        pass

    # Exit a parse tree produced by ToyLangParser#setOperator.
    def exitSetOperator(self, ctx:ToyLangParser.SetOperatorContext):
        pass


    # Enter a parse tree produced by ToyLangParser#conditionalOperator.
    def enterConditionalOperator(self, ctx:ToyLangParser.ConditionalOperatorContext):
        pass

    # Exit a parse tree produced by ToyLangParser#conditionalOperator.
    def exitConditionalOperator(self, ctx:ToyLangParser.ConditionalOperatorContext):
        pass


    # Enter a parse tree produced by ToyLangParser#elementOperator.
    def enterElementOperator(self, ctx:ToyLangParser.ElementOperatorContext):
        pass

    # Exit a parse tree produced by ToyLangParser#elementOperator.
    def exitElementOperator(self, ctx:ToyLangParser.ElementOperatorContext):
        pass


    # Enter a parse tree produced by ToyLangParser#comparisonOperator.
    def enterComparisonOperator(self, ctx:ToyLangParser.ComparisonOperatorContext):
        pass

    # Exit a parse tree produced by ToyLangParser#comparisonOperator.
    def exitComparisonOperator(self, ctx:ToyLangParser.ComparisonOperatorContext):
        pass


    # Enter a parse tree produced by ToyLangParser#logicalOperator.
    def enterLogicalOperator(self, ctx:ToyLangParser.LogicalOperatorContext):
        pass

    # Exit a parse tree produced by ToyLangParser#logicalOperator.
    def exitLogicalOperator(self, ctx:ToyLangParser.LogicalOperatorContext):
        pass


    # Enter a parse tree produced by ToyLangParser#unaryOperator.
    def enterUnaryOperator(self, ctx:ToyLangParser.UnaryOperatorContext):
        pass

    # Exit a parse tree produced by ToyLangParser#unaryOperator.
    def exitUnaryOperator(self, ctx:ToyLangParser.UnaryOperatorContext):
        pass


    # Enter a parse tree produced by ToyLangParser#funcOperator.
    def enterFuncOperator(self, ctx:ToyLangParser.FuncOperatorContext):
        pass

    # Exit a parse tree produced by ToyLangParser#funcOperator.
    def exitFuncOperator(self, ctx:ToyLangParser.FuncOperatorContext):
        pass


    # Enter a parse tree produced by ToyLangParser#emptySet.
    def enterEmptySet(self, ctx:ToyLangParser.EmptySetContext):
        pass

    # Exit a parse tree produced by ToyLangParser#emptySet.
    def exitEmptySet(self, ctx:ToyLangParser.EmptySetContext):
        pass


    # Enter a parse tree produced by ToyLangParser#uniSet.
    def enterUniSet(self, ctx:ToyLangParser.UniSetContext):
        pass

    # Exit a parse tree produced by ToyLangParser#uniSet.
    def exitUniSet(self, ctx:ToyLangParser.UniSetContext):
        pass



del ToyLangParser