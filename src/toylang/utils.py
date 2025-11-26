import sys
from pathlib import Path
from typing import cast, Optional

from antlr4 import (
    CommonTokenStream, 
    FileStream, 
    TerminalNode, 
    ParseTreeWalker
)
from antlr4.tree.Tree import TerminalNodeImpl as TerminalNode

from toylang.generated.ToyLangLexer import ToyLangLexer
from toylang.generated.ToyLangParser import ToyLangParser
from toylang.error_listener import ToyLangErrorListener
from toylang.semantic_analyzer import SemanticAnalyzer


def parse_file(
    filepath: Path,
    dump_tokens_filepath: Optional[Path] = None,
    dump_tree_filepath: Optional[Path] = None
):
    input_stream = FileStream(str(filepath))
    if dump_tokens_filepath is not None:
        dump_tokens(dump_tokens_filepath, input_stream)
        input_stream.seek(0)
    lexer = ToyLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ToyLangParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(ToyLangErrorListener())
    tree = cast(TerminalNode, parser.program())
    if dump_tree_filepath is not None:
        dump_tree(dump_tree_filepath, parser, tree)
    semantic_analyzer = SemanticAnalyzer()
    walker = ParseTreeWalker()
    walker.walk(semantic_analyzer, tree)
    if semantic_analyzer.errors:
        for error in semantic_analyzer.errors:
            print(error, file=sys.stderr)
        sys.exit(1)


def dump_tokens(dump_tokens_filepath, input_stream):
    lexer = ToyLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    stream.fill()
    with open(dump_tokens_filepath, 'w', encoding='utf-8') as f:
        for token in stream.tokens:
            token_name = lexer.symbolicNames[token.type]
            f.write(f"{token_name:<15} '{token.text}'\n")


def dump_tree(dump_tree_filepath, parser, tree):
    tree_str = get_tree(tree, parser)
    with open(dump_tree_filepath, 'w', encoding='utf-8') as f:
        f.writelines((s + '\n' for s in tree_str))


def get_tree(
    node: TerminalNode, 
    parser: ToyLangParser, 
    indent=0
) -> list[str]:
    rule_names = parser.ruleNames

    if hasattr(node, 'getRuleIndex'):
        rule_idx = node.getRuleIndex() # type: ignore
        rule_name = (
            rule_names[rule_idx] 
            if 0 <= rule_idx < len(rule_names) 
            else 'unknown'
        )
    else:
        rule_name = 'terminal'

    text = node.getText()

    result = []

    children: list[TerminalNode] | None = getattr(node, 'children', None)
    if (rule_name in ('WS', 'NEWLINE') 
        or text in (' ', '\t', '\n', '\r', '\f')
    ):
        pass 
    else:
        line = "│   " * indent
        if indent > 0:
            line += "├── "
        else:
            line += ""
        line += f"{rule_name}"
        if not children and text.strip():
            line += f": {repr(text)}"
        result.append(line)

    if children is not None: # type: ignore
        for child in node.children: # type: ignore
            child_result = get_tree(child, parser, indent + 1)
            result.extend(child_result)

    return result
