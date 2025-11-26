import sys

from antlr4.error.ErrorListener import ErrorListener


class ToyLangErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        lexer = recognizer.getTokenStream().tokenSource
        input_stream = lexer.inputStream
        text = input_stream.strdata
        lines = text.split('\n')
        error_line = lines[line - 1] if line <= len(lines) else ""

        error_msg = (
            f'  File "{input_stream.fileName}", line {line}\n' \
            f'    {error_line}\n' \
            f'    {" " * column}^\n' \
            f'SyntaxError: {msg}'
        )
        
        self.errors.append(error_msg)
        print(error_msg, file=sys.stderr)

    def has_errors(self):
        return len(self.errors) > 0