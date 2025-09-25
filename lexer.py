import ply.lex as lex

class CppLexer:
    # List of token names.   This is always required
    tokens = (
        'INTEGER', 'STRING',
        'IDENTIFIER',
        # Keywords: for|while|if|else|return|sum|int
        'FOR', 'WHILE', 'IF', 'ELSE', 'RETURN', 'SUM', 'INT',
        # Operators: +|-|=|<=|<|%|==|<<|>>|
        'PLUS', 'MINUS', 'ASSIGN', 'LEQ', 'LT', 'MOD', 'EQ', 'LEFT_SHIFT',
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
    # Integers
    def t_INTEGER(self, t):
            r'\d+'
            t.value = int(t.value)
            return t
    # Identifiers    
    def t_IDENTIFIER(self, t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        t.type = self.reserved.get(t.value, 'IDENTIFIER')
        return t
    # Operators
    t_EQ = r'=='
    t_ASSIGN = r'='
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_LEQ = r'<='
    t_LT = r'<'
    t_MOD = r'%'
    t_LEFT_SHIFT = r'<<'

    # Delimiters
    t_LBRACE = r'\{'
    t_RBRACE = r'\}'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_SEMICOLON = r';'

    t_ignore = ' \t'
    
    def build(self):
        return lex.lex(module=self)
    
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)
    
    def t_error(self, t):
        print(f"ERROR: Unrecognized character '{t.value[0]}' at line {t.lineno}")
        print(f"Hint: You might need to add this token to your lexer!")
        t.lexer.skip(1)
    

    def scan_file(self, filename):
        lexer = self.build()
        try:
            with open(filename, 'r') as f:
                content = f.read()
            
            lexer.input(content)
            tokens = []
            
            while True:
                tok = lexer.token()
                if not tok:
                    break
                tokens.append({
                    'type': tok.type,
                    'value': tok.value,
                    'lineno': tok.lineno
                })
            
            return tokens
        except FileNotFoundError:
            print(f"File {filename} not found")
            return []



lexer = lex.lex()