# Pascal Compiler Using Python
The City College of New York (CSC 42000) final project

## Author
Sajid Mahmud

# Requirements
- Download [python](https://www.python.org/downloads/) to run python scripts
- Download [mingw](https://www.mingw-w64.org/) for C compiler
- Download [git](https://git-scm.com/downloads) **OPTIONAL**

# Setting up and running the compiler
1. Clone the repo using the command **git clone https://sajidmahmud69/PascalCompiler.git** or download the repo as a zip folder
2. Open a terminal or a command prompt
3. Open the directory where the git repo is downloaded/cloned
4. Write the command **python pascal_compiler.py ./hello.pas** `NOTE: ./hello.pas is a sample pascal file that is provided with this git repo to showcase the compiler. To run your own pascal file just provide the file path in place of ./hello.pas`
5. If everything goes alright you will see the message **Parsing Completed** in the terminal/command prompt. This will generate a file "output.c"
6. Write the following command in the terminal **gcc output.c -o out**
7. The last command is:
    - For unix based users (mac, ubuntu) ---> **./out**
    - For windows users  ---> **out**
8. This will compile and execute the pascal file

## Notes about this compiler
This is a very simple pascal compiler written in python. The way it runs is it used the lexer to tokenize the words from the source file. The following are some examples of this token:
- Tk_PROGRAM
- TK_BEGIN
- TK_END
- TK_ADDITION
- TK_MULTIPLICATION

Once every word or reserved keyword is tokenized it then passes these tokens into the parser. Parser checks to see if all tokens form a valid syntax. If a valid syntax is formed it will then use the Emitter class to emit the pascal source code into a C code. Lastly, we can use the gcc compiler or mingw compiler to compile the C code created from the pascal file using our custom lexical analyzer and parser analyzer.
**NOTE: This compiler only handles how to print a statement into console and perform only float data type assignment and basic arithmetic operations**
