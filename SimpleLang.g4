grammar SimpleLang;

program
    : statement+ EOF
    ;

statement
    : assignmentStatement NEWLINE
    | whileStatement NEWLINE
    | ifStatement NEWLINE
    | NEWLINE
    ;

assignmentStatement
    : ID ASSIGN expression
    ;

whileStatement
    : WHILE expression DO (NEWLINE statement)* END
    ;

ifStatement
    : IF expression DO (NEWLINE statement)*
      (ELSE DO (NEWLINE statement)*)?
      END
    ;

// ----- Ausdrücke mit Vorrang -----
expression
    : comparisonExpr
    ;

comparisonExpr
    : additiveExpr ((EQ | NEQ | GT | LT | GE | LE) additiveExpr)*
    ;

additiveExpr
    : multiplicativeExpr ((PLUS | MINUS) multiplicativeExpr)*
    ;

multiplicativeExpr
    : primary ((MULT | DIV) primary)*
    ;

primary
    : ID
    | INTEGER_LITERAL
    | STRING_LITERAL
    | LPAREN expression RPAREN
    ;

// ----- LEXER -----
WHILE   : 'while' ;
DO      : 'do' ;
END     : 'end' ;
IF      : 'if' ;
ELSE    : 'else' ;

ASSIGN  : ':=' ;

EQ      : '==' ;
NEQ     : '!=' ;
GE      : '>=' ;
LE      : '<=' ;
GT      : '>' ;
LT      : '<' ;

PLUS    : '+' ;
MINUS   : '-' ;
MULT    : '*' ;
DIV     : '/' ;

LPAREN  : '(' ;
RPAREN  : ')' ;

ID      : [a-zA-Z_][a-zA-Z0-9_]* ;
INTEGER_LITERAL : [0-9]+ ;
STRING_LITERAL  : '"' (~["\r\n])* '"' ;

COMMENT : '#' ~[\r\n]* -> skip ;
WS      : [ \t]+ -> skip ;
NEWLINE : '\r'? '\n' ;
