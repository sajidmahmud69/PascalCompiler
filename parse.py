import sys
from lexer import Lexer

# Parser object keeps track of current token and checks if the code matches the program grammar

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer

        self.symbols = set ()           # variables declared so far
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


    # Return true if the current token is a comparison operator
    def isComparisonOperator (self):
        return \
            self.checkToken ('TK_GREATER_THAN') or \
            self.checkToken ('TK_GREATER_THAN_OR_EQUAL') or \
            self.checkToken ('TK_LESS_THAN') or \
            self.checkToken ('TK_LESS_THAN_OR_EQUAL') or \
            self.checkToken ('TK_EQUAL') or \
            self.checkToken ('TK_NOT_EQUAL')

    def abort(self, message):
        sys.exit("Error. " + message)



    def program (self):
        print ('PROGRAM')

        # We need to ignore some newlines as they maybe newlines inside the code for readability
        while self.checkToken ('TK_NEWLINE'):
            self.nextToken ()

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
            self.match ('TK_LEFT_PAREN')

            if self.checkToken ('TK_STRING'):
                # String
                self.nextToken ()
            else:
                # Expect an expression
                self.expression ()
            self.match ('TK_RIGHT_PAREN')

        elif self.checkToken ('TK_VAR'):
            self.nextToken ()

            # Check if identifier exists in symbols table, if not then declare it
            if self.curToken.text not in self.symbols:
                self.symbols.add (self.curToken.text)

            self.match ('TK_IDENTIFIER')
            self.match ('TK_ASSIGNMENT')

            self.expression ()


        else:
            print ('STATEMENT-END')
            self.match ('TK_END')
            self.match ('TK_PERIOD')
        
        # newline
        self.newline ()


    def comparison (self):
        print ('COMPARISON')

        self.expression ()
        # Must be at least one comparison operator and another expression.
        if self.isComparisonOperator():
            self.nextToken()
            self.expression()
        else:
            self.abort("Expected comparison operator at: " + self.curToken.text)

        # Can have 0 or more comparison operator and expressions
        while self.isComparisonOperator ():
            self.nextToken ()
            self.expression ()



    def expression (self):
        print ('EXPRESSION')

        self.term ()
        # Can have 0 or more +/- and expressions
        while self.checkToken ('TK_ADDITION') or self .checkToken ('TK_SUBTRACTION'):
            self.nextToken ()
            self.term ()

    

    def term (self):
        print ('TERM')
        self.unary ()
        # Can have 0 or more*// expressions
        while self.checkToken ('TK_MULTIPLICATION') or self.checkToken ('TK_DIVISION'):
            self.nextToken ()
            self.unary ()



    def unary (self):
        print ('UNARY')
        # Optional +/-
        if self.checkToken ('TK_ADDITION') or self.checkToken ('TK_SUBTRACTION'):
            self.nextToken ()
        self.primary ()



    def primary (self):
        print ('PRIMARY (' + self.curToken.text + ')')
        if self.checkToken ('TK_NUMBER'):
            self.nextToken ()
        elif self.checkToken ('TK_IDENTIFIER'):
            # make sure the variable already exists
            if self.curToken.text not in self.symbols:
                self.abort ('Referencing variable before assignment: ' + self.curToken.text)
            self.nextToken ()
        else:
            # Error!
            self.abort("Unexpected token at " + self.curToken.text)



    def newline (self):
        # print ("NEWLINE")

        # Require at least one newline.
        self.match('TK_NEWLINE')
        # But we will allow extra newlines too, of course.
        while self.checkToken('TK_NEWLINE'):
            self.nextToken()