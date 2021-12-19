import sys
from lexer import Lexer
from parse import Parser
from lex import RESERVED_KEYWORD_DICT
from enum import Enum


def main ():
    # user_input = "+- */ % >= <> < <= > >= ="
    # user_input = '+ - > >= "hello" 1435'
    # user_input = 'if else + / 123  variable "bye"'
    print ('========================= Pascal Compiler ===========================')
    # if len (sys.argv) != 2:
    #     sys.exit ("Error: Compiler needs source file as argument")
    # with open (sys.argv[1], 'r') as src_file:
    #     input_file = src_file.read ()

    # # Initialize the lexer and parser
    # lexer = Lexer (input_file)
    # parser = Parser (lexer)

    # parser.program ()       # start the parser
    # print ('Parsing completed')

    user_input = '( = )'
    lexer = Lexer (user_input)
    token = lexer.getToken ()
    while token.kind != 'TK_EOF':
        print (token.kind)
        token = lexer.getToken ()
 

    print ('========================= Pascal Compiler ===========================')

if __name__ == '__main__':
    main ()

