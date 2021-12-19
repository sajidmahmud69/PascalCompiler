# TODO: 
from lexer import Lexer
from lex import RESERVED_KEYWORD_DICT
from enum import Enum


def main ():
    # user_input = "+- */ % >= <> < <= > >= ="
    user_input = '+ - > >= "hello"'
    lexer = Lexer (user_input)
    token = lexer.getToken ()
    while token.kind != 'TK_EOF':
        print (token.kind)
        token = lexer.getToken ()

if __name__ == '__main__':
    main ()
