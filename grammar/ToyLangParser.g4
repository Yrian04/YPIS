parser grammar ToyLangParser;
options { tokenVocab=ToyLangLexer; }

program
    : vars? subprograms? body?
    ;

vars
    : (assignment NEWLINE | NEWLINE)+
    ;

subprograms
    : (subprogram | NEWLINE)+
    ;

body
    : (statement | NEWLINE)+
    ;

subprogram
    : in_params? ID out_params? COLON block
    ;

statement
    : simple_statement (SEMICOLON simple_statement)* SEMICOLON? (NEWLINE | EOF)
    | compound_statement
    ;

simple_statement
    : assignment 
    | call 
    | PASS  
    ;

assignment
    : ID EQUAL expr
    ;

call
    : (expr (COMMA expr)*)? ARROW ID (ARROW ID (COMMA ID)*)?
    ;

compound_statement
    : if_
    | for_
    | while_
    | until_
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
    | NEWLINE INDENT statement+  DEDENT
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
    : set_
    | bool_
    ;

set_
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

bool_
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
    | NOT_IN
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

funcOperator
    : ARROW
    ;

emptySet
    : LBRACE RBRACE
    ;

uniSet
    : LBRACE DOTDOT RBRACE
    ;
