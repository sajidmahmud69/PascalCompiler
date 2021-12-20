from enum import Enum
# Token contains the original text and the type of token.
class Token:   
    def __init__(self, tokenText, tokenKind):
        self.text = tokenText   # The token's actual text. Used for identifiers, strings, and numbers.
        self.kind = tokenKind   # The TokenType that this token is classified as.
    
    @staticmethod
    def check_if_keyword (tokenText):
        if tokenText in RESERVED_KEYWORD_DICT:
            return RESERVED_KEYWORD_DICT [tokenText]
        return None



RESERVED_KEYWORD_DICT = {
    'program': 'TK_PROGRAM',
    'var': 'TK_VAR',
    'begin': 'TK_BEGIN',
    'end': 'TK_END',
    'for': 'TK_FOR',
    'if': 'TK_IF',
    'else': 'TK_ELSE',
    'then': 'TK_THEN',
    'while': 'TK_WHILE',
    'writeln': 'TK_WRITELN',
    'TK_NEWLINE': 'TK_NEWLINE',
    'TK_EOF': 'TK_EOF'
}

DATA_TYPE_DICT = {
    'integer': 'TK_TYPE_INT',
    'boolean': 'TK_TYPE_BOOL',
    'string': 'TK_TYPE_STRING',
    'real': 'TK_TYPE_REAL'
}

OPERATOR_DICT = {
    # Assignment operator
    ':=' : 'TK_ASSIGNMENT',
    
    # Arithmetic operators
    '+': 'TK_ADDITION',
    '-': 'TK_SUBTRACTION',
    '*': 'TK_MULTIPLICATION',
    '/': 'TK_DIVISION',
    '%': 'TK_MODULUS',

    # Relational Operators
    '=': 'TK_EQUAL',
    '>': 'TK_GREATER_THAN',
    '<': 'TK_LESS_THAN',
    '>=': 'TK_GREATER_THAN_OR_EQUAL',
    '<=': 'TK_LESS_THAN_OR_EQUAL',
    '<>': 'TK_NOT_EQUAL',


    # Boolean Operator
    'and': 'TK_AND',
    'or': 'TK_OR',
    'not': 'TK_NOT',

    # Miscellaneous
    '(': 'TK_LEFT_PAREN',
    ')': 'TK_RIGHT_PAREN',
    ';': 'TK_SEMICOLON',
    '.': 'TK_PERIOD'
}

# TokenType = Enum ('TokenType', [
#         ('ADDITION', '+'),
#         ('SUBTRACTION', '-'),
#         ('NEWLINE', '\n'),
#         ('EOF', '\0')
#     ])

# # print (TokenType.EOF)