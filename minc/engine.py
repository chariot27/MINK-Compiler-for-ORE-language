import inout
import os
import variables

# descobrir por não imprimi os valores do input no impout
# adicionar comentários ao codigo

class Token:
    def __init__(self, type="", value=None):
        self.type = type
        self.value = value
    def __repr__(self):
        return "<Token " + str(self.type) + ">" if self.value == None else "<Token " + str(self.type) + ":" + str(self.value) + ">"

#  NÚMEROS 
numbers = "0123456789"

#  SINAIS
point = "."
plus = "+"
minus = "-"
multiply = "*"
divide = "/"
mod = "%"

class Lexer:
    def __init__(self):
        self.pos = 0
        self.txt = ""
        self.char = ""
    def __call__(self, txt):
        self.txt = txt
        self.pos = -1
        self.char = None
        self.next()
        tokens = []
        while self.char != None:
            self.skip_white_spaces()
            if self.char in numbers + point:
                tok = Token("Value")
                n = self.char + ""
                self.next()
                ok = False
                while self.char != None and self.char in numbers + point:
                    if len(n) == 1 and n == ".":
                        ok = True
                    if self.char == ".":
                        if ok:
                            pass
                        ok = True
                    n += self.char
                    self.next()
                if ok:
                    tok.value = float(n)
                else:
                    tok.value = int(n)
                tokens.append(tok)
                continue
            elif self.char == plus:
                tokens.append(Token("+"))
            elif self.char == minus:
                tokens.append(Token("-"))
            elif self.char == multiply:
                tokens.append(Token("*"))
            elif self.char == divide:
                tokens.append(Token("/"))
            elif self.char == mod:
                tokens.append(Token("%"))
            elif self.char in ['"', "'"]:
                self.next()
                st = ""
                while self.char != None and self.char not in ['"', "'"]:
                    st += self.char
                    self.next()
                self.next()
                tokens.append(Token("STRING", st))
            else:
                raise Exception(f"Caractere inválido: {self.char}")
            self.next()
        return tokens
    
    def skip_white_spaces(self):
        while self.char != None and self.char == " ":
            self.next()
    def next(self):
        self.pos += 1
        if self.pos >= len(self.txt):
            self.char = None
        else:
            self.char = self.txt[self.pos]
            
class Node:
    def __init__(self, type="", value=None):
        self.type = type
        self.value = value
    def __repr__(self):
        return "<Node " + str(self.type) + ">" if self.value == None else "<Node " + str(self.type) + ":" + str(self.value) + ">"
    
class Parser:
    def __init__(self):
        self.tok_pos = 0
        self.tok = None
        self.tokens = []
    def __call__(self,tokens):
        self.tok_pos = -1
        self.tokens = tokens
        self.tok = None
        self.nextTok()
        return self.expr()
    def expr(self):
        re = self.term()
        return re
    def term(self):
        re = self.factor()
        while self.tok != None:
            if self.tok.type == "+":
                self.nextTok()
                re = Node("+", [re, self.term()])
            elif self.tok.type == "-":
                self.nextTok()
                re = Node("-", [re, self.term()])
            elif self.tok.type == "*":
                self.nextTok()
                re = Node("*", [re, self.term()])
            elif self.tok.type == "/":
                self.nextTok()
                re = Node("/", [re, self.term()])
            elif self.tok.type == "%":
                self.nextTok()
                re = Node("%", [re, self.term()])
        return re

    def factor(self):
        tok = self.tok
        if self.tok.type == "Value":
            self.nextTok()
            return Node("Value", tok.value)
        elif self.tok.type == "-":
            self.nextTok()
            return Node("inverseNumber", self.factor())
        elif self.tok.type == "STRING":
            tok = self.tok
            self.nextTok()
            return Node("STRING", tok.value)
        else:
            raise Exception("Erro de sintaxe")
    def __call__(self, tokens):
        self.tok_pos = -1
        self.tokens = tokens
        self.tok = None
        self.nextTok()
        return self.expr()
    def nextTok(self):
        self.tok_pos += 1
        if self.tok_pos >= len(self.tokens):
            self.tok = None
        else:
            self.tok = self.tokens[self.tok_pos]
class Interpreter:
    def __init__(self):
        self.globals = {}
        self.lexer = Lexer()
        self.parser = Parser()
    def process(self, txt):
        return self.parser(self.lexer(txt))
    def eval(self, txt, l={}, inum=0):
        nodes = self.process(txt)
        return self.exec_node(nodes, l, inum)
    def exec_node(self, node: Node, l: dict, inum: int):
        if node.type == "Value":
            return node.value
        elif node.type == "inverseNumber":
            return -self.exec_node(node.value, l, inum)
        elif node.type == "STRING":
            return node.value
        elif node.type == "+":
            return self.exec_node(node.value[0], l, inum) + self.exec_node(node.value[1], l, inum)
        elif node.type == "-":
            return self.exec_node(node.value[0], l, inum) - self.exec_node(node.value[1], l, inum)
        elif node.type == "*":
            return self.exec_node(node.value[0], l, inum) * self.exec_node(node.value[1], l, inum)
        elif node.type == "/":
            return self.exec_node(node.value[0], l, inum) / self.exec_node(node.value[1], l, inum)
        elif node.type == "%":
            return self.exec_node(node.value[0], l, inum) % self.exec_node(node.value[1], l, inum)

if __name__==("__main__"):
    variaveis = {}
    with open("test.ore", "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if "=" in linha:
                nome_variavel, valor = linha.split("=")
                nome_variavel = nome_variavel.strip()
                valor = valor.strip()
                if valor.startswith('"') and valor.endswith('"'):
                    valor = valor[1:-1]  # remove aspas
                else:
                    try:
                        valor = eval(valor)  # avalia a expressão como uma conta
                    except Exception as e:
                        print(f"Erro ao avaliar expressão: {e}")
                        valor = None
                variaveis[nome_variavel] = valor
            elif linha.startswith("impout"):
                linha_original = linha[7:-1]  # remove "impout(" e ")"
                while "{" in linha_original and "}" in linha_original:
                    start = linha_original.index("{")
                    end = linha_original.index("}")
                    variavel = linha_original[start+1:end]
                    if variavel in variaveis:
                        linha_original = linha_original.replace("{" + variavel + "}", str(variaveis[variavel]))
                    else:
                        linha_original = linha_original.replace("{" + variavel + "}", "Variável não definida")
                print(linha_original[1:-1])
            