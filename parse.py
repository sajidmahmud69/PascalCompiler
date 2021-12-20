import sys
from lexer import Lexer

# Parser object keeps track of current token and checks if the code matches the program grammar

class Parser:
    def __init__(self, lexer, emitter):
        self.lexer = lexer
        self.emitter = emitter

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
        self.emitter.headerLine ('#include <stdio.h>')
        self.emitter.headerLine ('int main (void){')

        # We need to ignore some newlines as they maybe newlines inside the code for readability
        while self.checkToken ('TK_NEWLINE'):
            self.nextToken ()

        # Parse all the statements in the program
        while not self.checkToken ('TK_EOF'):
            self.statement()

        self.emitter.emitLine ('return 0;')
        self.emitter.emitLine ('}')


    def statement (self):
        # Check the first token to see what kind of token it is

        # Check if program keyword is here
        if self.checkToken ('TK_PROGRAM'):
            self.nextToken ()
            self.match ('TK_IDENTIFIER')
            self.match ('TK_SEMICOLON')
            self.match ('TK_NEWLINE')
            self.match ('TK_BEGIN')
            # self.match ('TK_NEWLINE')
            
        # writeln (expression | string)
        elif self.checkToken ('TK_WRITELN'):
            self.nextToken ()
            self.match ('TK_LEFT_PAREN')

            if self.checkToken ('TK_STRING'):
                # String
                self.emitter.emitLine ("printf(\"" + self.curToken.text + "\\n\");")
                self.nextToken ()
            else:
                # Expect an expression
                self.emitter.emit ("printf(\"%" + ".2f\\n\", (float)(")
                self.expression ()
                self.emitter.emitLine ("));")
            self.match ('TK_RIGHT_PAREN')
            self.match ('TK_SEMICOLON')

        # var identifier = expression
        elif self.checkToken ('TK_VAR'):
            self.nextToken ()

            # Check if identifier exists in symbols table, if not then declare it
            if self.curToken.text not in self.symbols:
                self.symbols.add (self.curToken.text)
                self.emitter.headerLine ("float " + self.curToken.text + ";")
            self.emitter.emit (self.curToken.text + " = ")
            self.match ('TK_IDENTIFIER')
            self.match ('TK_ASSIGNMENT')


            self.expression ()
            self.emitter.emitLine (";")


        else:
            self.match ('TK_END')
            self.match ('TK_PERIOD')
        
        # newline
        self.newline ()


    def comparison (self):
        self.expression ()
        # Must be at least one comparison operator and another expression.
        if self.isComparisonOperator():
            self.emitter.emit(self.curToken.text)
            self.nextToken()
            self.expression()
        else:
            self.abort("Expected comparison operator at: " + self.curToken.text)

        # Can have 0 or more comparison operator and expressions
        while self.isComparisonOperator ():
            self.emitter.emit(self.curToken.text)
            self.nextToken ()
            self.expression ()



    def expression (self):
        self.term ()
        # Can have 0 or more +/- and expressions
        while self.checkToken ('TK_ADDITION') or self .checkToken ('TK_SUBTRACTION'):
            self.emitter.emit (self.curToken.text)
            self.nextToken ()
            self.term ()

    

    def term (self):
        self.unary ()
        # Can have 0 or more*// expressions
        while self.checkToken ('TK_MULTIPLICATION') or self.checkToken ('TK_DIVISION'):
            self.emitter.emit (self.curToken.text)
            self.nextToken ()
            self.unary ()



    def unary (self):
        # Optional +/-
        if self.checkToken ('TK_ADDITION') or self.checkToken ('TK_SUBTRACTION'):
            self.emitter.emit (self.curToken.text)
            self.nextToken ()
        self.primary ()



    def primary (self):
        if self.checkToken ('TK_NUMBER'):
            self.emitter.emit (self.curToken.text)
            self.nextToken ()
        elif self.checkToken ('TK_IDENTIFIER'):
            # make sure the variable already exists
            if self.curToken.text not in self.symbols:
                self.abort ('Referencing variable before assignment: ' + self.curToken.text)
            self.emitter.emit (self.curToken.text)
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