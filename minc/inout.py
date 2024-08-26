# ENTRADA E SAÍDA
impout = "impout" # CHECK
inlex = "inlex"

class Lexer:
    def __init__(self, txt):
        self.txt = txt
        self.pos = 0
        self.tokens = []
        self.tok_pos = 0

    def nextTok(self):
        while self.pos < len(self.txt):
            if self.txt[self.pos] == " ":
                self.pos += 1
                continue
            if self.txt[self.pos] == "(":
                self.tokens.append(Token("LPAREN", "("))
                self.pos += 1
                continue
            if self.txt[self.pos] == ")":
                self.tokens.append(Token("RPAREN", ")"))
                self.pos += 1
                continue
            if self.txt[self.pos] == "\"":
                self.pos += 1
                string = ""
                while self.txt[self.pos] != "\"":
                    string += self.txt[self.pos]
                    self.pos += 1
                self.tokens.append(Token("STRING", string))
                self.pos += 1
                continue
            if self.txt[self.pos:].startswith("impout"):
                self.tokens.append(Token("IMPout", "impout"))
                self.pos += 6
                continue
            raise Exception("Erro de sintaxe")
        return self.tokens

    def __call__(self):
        while self.pos < len(self.txt):
            self.nextTok()
        return self.tokens

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.tokens = []
        self.tok_pos = 0
        if self.tokens:
            self.tok = self.tokens[self.tok_pos]
        else:
            self.tok = None

    def eat(self, token_type):
        if self.tok and self.tok.type == token_type:
            self.tok_pos += 1
            if self.tok_pos < len(self.tokens):
                self.tok = self.tokens[self.tok_pos]
            else:
                self.tok = None
        else:
            raise Exception("Erro de sintaxe")

    def expr(self):
        if self.tok and self.tok.type == "IMPout":
            self.eat("IMPout")
            self.eat("LPAREN")
            string_token = self.tok
            self.eat("STRING")
            self.eat("RPAREN")
            return string_token.value
        else:
            if self.tok:
                raise Exception(f"Erro de sintaxe: token '{self.tok.value}' não esperado")
            else:
                raise Exception("Erro de sintaxe: fim de arquivo inesperado")

    def __call__(self, txt):
        self.lexer.txt = txt
        self.tokens = self.lexer()
        self.tok_pos = 0
        if self.tokens:
            self.tok = self.tokens[self.tok_pos]
        else:
            self.tok = None
        return self.expr()

class Interpreter:
    def __init__(self, lexer, parser):
        self.lexer = lexer
        self.parser = parser

    def eval(self, txt, l={}, inum=0):
        result = self.parser(txt)  # Chama o método __call__ do parser
        return result
    
    def execute_file(self, filename):
        with open(filename, 'r') as f:
            for linha in f:
                self.execute(linha.strip())
                
    
    def execute(self, code):
        # Remova os parênteses extras da linha
        code = code.strip('()')
        # Execute o código com o interpretador impout
        result = eval(code)
        print(result)
            
    
def create_interpreter():
    lexer = Lexer("")
    parser = Parser(lexer)
    return Interpreter(lexer, parser)