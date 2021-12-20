# This file will keep track of generated C code and outputs it
class Emitter:
    def __init__(self, path):
        self.path = path
        self.header = ''
        self.code = ''

    def emit (self, code):
        self.code += code

    def emitLine (self, code):
        self.code += code + '\n'

    def headerLine (self, code):
        self.header += code + '\n'

    def writeFile (self):
        with open (self.path, 'w') as outputFile:
            outputFile.write (self.header + self.code)

    