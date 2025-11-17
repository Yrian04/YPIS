parser grammar ToyLangParser;
options { tokenVocab=ToyLangLexer; }

program
    : (statement | NEWLINE)* EOF
    ;

subprogram
    : in_params? ID out_params? COLON NEWLINE block
    ;

statement
    : simple_statement
    | compound_statement
    ;

simple_statement
    : assignment
    | PASS
    ;

assignment
    : expr ARROW ID
    ;

compound_statement
    : if_
    | for_
    | while_
    | until_
    | subprogram
    ;

if_
    : IF expr COLON block 
    ( ELIF expr COLON block )* 
    ( ELSE COLON block )?
    ;

for_
    : FOR ID IN expr COLON block
    ;

while_
    : WHILE expr COLON block
    ;

until_
    : DO COLON block UNTIL expr
    ;

block
    : simple_statement
    | NEWLINE INDENT statement+ DEDENT
    ;

call
    : call_in_params? ID subcall* call_out_params?
    ;

subcall
    : ARROW call_in_params ID
    ;

call_in_params
    : expr (COMMA expr)* ARROW
    ;

call_out_params
    : ARROW expr (COMMA expr)*
    ;

expr
    : expr setOperator expr
    | expr conditionalOperator expr
    | expr logicalOperator expr
    | unaryOperator expr
    | LPAREN expr RPAREN
    | atom
    ;

atom
    : literal
    | ID
    ;

literal
    : STRING
    | set
    | bool
    ;

set
    : LBRACE atom (COMMA atom)* RBRACE
    | emptySet
    | uniSet
    ;

in_params
    : ID (COMMA ID)* ARROW
    ;

out_params
    : ARROW ID (COMMA ID)*
    ;

bool
    : TRUE
    | FALSE
    ;

setOperator
    : UNION
    | INTERSECTION
    | CARTESIAN
    | DIFFERENCE
    ;

conditionalOperator
    : elementOperator
    | comparisonOperator
    ;

elementOperator
    : IN
    ;

comparisonOperator
    : EQ
    | NE
    | GT
    | LT
    | GE
    | LE
    ;

logicalOperator
    : AND
    | OR
    | XOR
    ;

unaryOperator
    : NOT
    ;

emptySet
    : LBRACE RBRACE
    ;

uniSet
    : LBRACE DOTDOT RBRACE
    ;
