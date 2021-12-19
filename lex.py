from enum import Enum
# Token contains the original text and the type of token.
class Token:   
    def __init__(self, tokenText, tokenKind):
        self.text = tokenText   # The token's actual text. Used for identifiers, strings, and numbers.
        self.kind = tokenKind   # The TokenType that this token is classified as.



RESERVED_KEYWORD_DICT = {
    'program': 'TK_PROGRAM',
    'var': 'TK_VAR',
    'begin': 'TK_BEGIN',
    'end': 'TK_END',
    'for': 'TK_FOR',
    'if': 'TK_IF',
    'else': 'TK_ELSE',
    'while': 'TK_WHILE',
    'writeln': 'TK_WRITELN',
    # '\\n': 'TK_NEWLINE',
    # '\\0': 'TK_EOF'
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
    'not': 'TK_NOT'
}

# TokenType = Enum ('TokenType', [
#         ('ADDITION', '+'),
#         ('SUBTRACTION', '-'),
#         ('NEWLINE', '\n'),
#         ('EOF', '\0')
#     ])

# # print (TokenType.EOF)