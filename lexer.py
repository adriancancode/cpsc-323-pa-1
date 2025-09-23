import ply.lex as lex


tokens = (
    'INTEGER', 'STRING',
    'IDENTIFIER',
    # Keywords: for|while|if|else|return|sum|int
    'FOR', 'WHILE', 'IF', 'ELSE', 'RETURN', 'SUM', 'INT',
    # Operators: +|-|=|<=|<|%|
    'PLUS', 'MINUS', 'EQUALS', 'LEQ', 'LT', 'MOD',
    # Delimiters: { | } | ( | ) | ; | 
    'LBRACE', 'RBRACE', 'LPAREN', 'RPAREN', 'SEMICOLON',
    'COMMENT'

)

# For keywords
reserved = {
    'for': 'FOR',
    'while':'WHILE',
    'if':'IF',
    'else':'ELSE',
    'return':'RETURN',
    'sum':'SUM',
    'int':'INT'
}

tokens += list(reserved.values())

t_OPERA

lexer = lex.lex()