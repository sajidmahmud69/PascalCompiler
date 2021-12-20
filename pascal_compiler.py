import sys
from lexer import Lexer
from parse import Parser
from emitter import Emitter


def main ():
    # user_input = "+- */ % >= <> < <= > >= ="
    # user_input = '+ - > >= "hello" 1435'
    # user_input = 'if else + / 123  variable "bye"'
    print ('========================= Pascal Compiler ===========================')
    if len (sys.argv) != 2:
        sys.exit ("Error: Compiler needs source file as argument")
    with open (sys.argv[1], 'r') as src_file:
        input_file = src_file.read ()

    # Initialize the lexer, emitter and parser
    lexer = Lexer (input_file)
    emitter = Emitter ('output.c')
    parser = Parser (lexer, emitter)

    parser.program ()       # start the parser
    emitter.writeFile ()    # write the output to the file 
    print ('Parsing completed')

    # user_input = '( = ) ; . abcdf'
    # lexer = Lexer (user_input)
    # token = lexer.getToken ()
    # while token.kind != 'TK_EOF':
    #     print (token.kind)
    #     token = lexer.getToken ()
 

    print ('========================= Pascal Compiler ===========================')

if __name__ == '__main__':
    main ()

