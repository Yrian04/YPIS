lexer grammar ToyLangLexer ;
tokens { 
    INDENT, 
    DEDENT 
}
options{
    superClass = ToyLangLexerBase;
}
// keywords
OUT : 'out' ;
DO : 'do' ;
FOR : 'for' ;
IN : 'in' ;
WHILE : 'while' ;
UNTIL : 'until' ;
IF : 'if' ;
ELIF : 'elif' ;
ELSE : 'else' ;
TRUE  : 'true' ;
FALSE : 'false' ;
PASS : 'pass' ;
// set operators
UNION : '+' ;
INTERSECTION : '*' ;
CARTESIAN : '@' ;
DIFFERENCE : '\\' ;
// comparison operators
EQ : '=' ;
NE : '<>' ;
GT : '>' ;
LT : '<' ;
GE : '>=' ;
LE : '<=' ;
// logical operators
NOT : 'not' ;
AND : 'and' ;
OR : 'or' ;
XOR : 'xor' ;
//
ARROW : '->' ;
// punctuation
COLON : ':' ;
SEMICOLON : ';' ;
COMMA : ',' ;
LPAREN : '(' {self.openBrace();};
RPAREN : ')' {self.closeBrace();};
LBRACE : '{' {self.openBrace();};
RBRACE : '}' {self.closeBrace();};
LBRACK : '[' {self.openBrace();};
RBRACK : ']' {self.closeBrace();};
DOTDOT : '..' ;

NEWLINE: ({self.atStartOfInput()}? SPACES | ( '\r'? '\n' | '\r' | '\f') SPACES?) {self.onNewLine();};

ID: [a-zA-Z_0-9]+ ;

STRING
    : '\'' (~['\r\n\\] | '\\' .)* '\''
    | '"' (~["\r\n\\] | '\\' .)* '"'
    ;

SKIP_: ( SPACES | COMMENT ) -> skip;
    
fragment SPACES: [ \t]+;

fragment COMMENT: '//' ~[\r\n\f]*;