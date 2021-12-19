import sys
from lex import Token, RESERVED_KEYWORD_DICT, DATA_TYPE_DICT, OPERATOR_DICT
class Lexer:
    def __init__(self, user_input):
        self.source = user_input + '\n' # Source code to lex as a string. Append a newline to simplify parsing the last token/statement.
        self.curChar = ''   # Current character in the string.
        self.curPos = -1    # Current position in the string.
        self.nextChar()

    # Process the next character
    def nextChar (self):
        self.curPos += 1                # increment the current position by 1
        # if curr pos == len of file then you have reached the end of the file and set the 
        # current character to null character
        if self.curPos >= len(self.source):
            self.curChar = '\0'  # EOF
        else:
            self.curChar = self.source[self.curPos]

    # Return the lookahead character.
    def peek(self):
        # get the character by 1 position ahead of the current character
        if self.curPos + 1 >= len(self.source):                 # if current position == len of file or exceeds length of file return null character
            return '\0'
        return self.source[self.curPos+1]

    # Invalid token found, print error message and exit.
    def abort(self, message):
        sys.exit ("Lexing error. " + message)
		
    # Skip whitespace except newlines, which we will use to indicate the end of a statement.
    def skipWhitespace(self):
        while self.curChar == ' ' or self.curChar == '\t' or self.curChar == '\r':
            self.nextChar()



    # Return the next token.
    def getToken(self):
        self.skipWhitespace ()
        token = None


        # See if we can use the first character to find out what kind of token it is
        # If it's multiple character to make an operator we will process it later
        if self.curChar == '+':
            token = Token (self.curChar, OPERATOR_DICT['+'])
        elif self.curChar == '-':
            token = Token (self.curChar, OPERATOR_DICT['-'])
            
        elif self.curChar == '*':
            token = Token (self.curChar, OPERATOR_DICT['*'])
            
        elif self.curChar == '/':
            token = Token (self.curChar, OPERATOR_DICT['/'])

        elif self.curChar == '%':
            token = Token (self.curChar, OPERATOR_DICT['%'])
        
        elif self.curChar == '=':
            token = Token (self.curChar, OPERATOR_DICT ['='])
        
        elif self.curChar == '>':
            # Check whether it is > or >= 
            if self.peek () == '=':
                lastChar = self.curChar
                self.nextChar ()
                token = Token (lastChar + self.curChar, OPERATOR_DICT ['>='])
            else:
                token = Token (self.curChar, OPERATOR_DICT ['>'])

        elif self.curChar == '<':
            # Check whether this token is < or <> or <=
            if self.peek () == '>':
                lastChar = self.curChar
                self.nextChar ()
                token = Token (lastChar + self.curChar, OPERATOR_DICT ['<>'])
            elif self.peek () == '=':
                lastChar = self.curChar
                self.nextChar ()
                token = Token (lastChar + self.curChar, OPERATOR_DICT ['<='])  
            else:
                token = Token (self.curChar, OPERATOR_DICT ['<'])

        elif self.curChar == ':':
            if self.peek () == '=':
                lastChar = self.curChar
                self.nextChar ()
                token = Token (lastChar + self.curChar, OPERATOR_DICT [':='])
        
        # handle string
        elif self.curChar == '"':
            # Get next character between quotations
            self.nextChar ()
            startPos = self.curPos 
            

            while self.curChar != '"':
                # Don't allow special characters in the string. No escape characters, newlines, tabs, or %.
                if self.curChar == '\r' or self.curChar == '\n' or self.curChar == '\t' or self.curChar == '\\' or self.curChar == '%':
                    self.abort("Illegal character in string.")
                self.nextChar()

            tokText = self.source[startPos : self.curPos] # Get the substring.
            token = Token(tokText, 'TK_STRING')


        # handle numbers
        elif self.curChar.isdigit ():
            # Leading character is a digit, so this must be a number.
            # Get all consecutive digits and decimal if there is one.
            startPos = self.curPos
            while self.peek ().isdigit ():
                self.nextChar ()

            if self.peek () == '.':         # decimal
                self.nextChar ()

                # Must have at least one digit after decimal.
                if not self.peek().isdigit(): 
                    # Error!
                    self.abort("Illegal character in number.")
                while self.peek ().isdigit ():
                    self.nextChar ()

            tokText = self.source [startPos: self.curPos + 1]   # get the substring aka number
            token = Token (tokText, 'TK_NUMBER')

        # handle identifiers such as variables
        elif self.curChar.isalpha ():
            # Leading character is a letter so this could be either an identifier or keyword
            # Get the rest of the alpha numeric characters
            startPos = self.curPos
            while self.peek ().isalnum():
                self.nextChar ()

            # Check to see if the token is in the list of keywords
            tokText = self.source[startPos : self.curPos + 1]       # get the substring
            keyword = Token.check_if_keyword (tokText)
            if keyword is None:     # Identifier/Variable
                token = Token (tokText, 'TK_IDENTIFIER')
            else:
                token = Token (tokText, keyword)



        elif self.curChar == '\n':
            token = Token (self.curChar, 'TK_NEWLINE')
            
        elif self.curChar == '\0':
            token = Token (self.curChar, 'TK_EOF')
            
        else:
            # Unknown token!
            self.abort("Unknown token: " + self.curChar)
			
        self.nextChar()
        return token