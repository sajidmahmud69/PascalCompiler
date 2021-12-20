import sys
from lexer import Lexer

# Parser object keeps track of current token and checks if the code matches the program grammar

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.curToken = None
        self.peekToken = None
        self.nextToken()
        self.nextToken()    # Call this twice to initialize current and peek.

    # Return true if the current token matches.
    def checkToken(self, kind):
        return kind == self.curToken.kind

    # Return true if the next token matches.
    def checkPeek(self, kind):
        return kind == self.peekToken.kind
        

    # Try to match current token. If not, error. Advances the current token.
    def match(self, kind):
        if not self.checkToken(kind):
            self.abort ("Expected " + kind + ", got " + self.curToken.kind)
        self.nextToken ()

    # Advances the current token.
    def nextToken(self):
        self.curToken = self.peekToken
        self.peekToken = self.lexer.getToken()
        # No need to worry about passing the EOF, lexer handles that.

    def abort(self, message):
        sys.exit("Error. " + message)



    def program (self):
        print ('PROGRAM')

        # Parse all the statements in the program
        while not self.checkToken ('TK_EOF'):
            self.statement()


    def statement (self):
        # Check the first token to see what kind of token it is

        # Check if program keyword is here
        if self.checkToken ('TK_PROGRAM'):
            print ('STATEMENT-PROGRAM')
            self.nextToken ()
            self.match ('TK_IDENTIFIER')
            self.match ('TK_SEMICOLON')
            self.match ('TK_NEWLINE')
            self.match ('TK_BEGIN')
            # self.match ('TK_NEWLINE')
            
        # writeln (expression | string)
        elif self.checkToken ('TK_WRITELN'):
            print ('STATEMENT-WRITELN')
            self.nextToken ()

            if self.checkToken ('TK_STRING'):
                # String
                self.nextToken ()
            else:
                # Expect an expression
                self.expression ()

        # if condiition
        elif self.checkToken ('TK_IF'):
            print ('STATEMENT_IF')
            self.nextToken ()
            self.comparison ()

            self.match ('TK_THEN')
            self.newline ()

            # Zero or more statements in the if body
            while not self.checkToken ('TK_')

        # last token must be TK_END followed by TK_PERIOD
        else:
            print ('STATEMENT-END')
            self.match ('TK_END')
            self.match ('TK_PERIOD')
        
        # newline
        self.newline ()

    def newline (self):
        # print ("NEWLINE")

        # Require at least one newline.
        self.match('TK_NEWLINE')
        # But we will allow extra newlines too, of course.
        while self.checkToken('TK_NEWLINE'):
            self.nextToken()