import re

# já atribui inteiros 
# já atribui strings 
# falta atribuir floats
# falta atribuir contas matemáticas
# falta atribuir variaveis na saida de impout exemplo = impout(var) || impout("o nome é: {}".format(var))
# falta atribuir listas
# falta atribuir matrizes


class AtribuidorDeVariaveis:
    def __init__(self, lexer, parser):
        self.lexer = lexer
        self.parser = parser
        self.variaveis = {}

    def atribuir(self, nome_var, valor):
        self.variaveis[nome_var] = valor

    def get_variavel(self, nome_var):
        return self.variaveis.get(nome_var)

    def executar_codigo(self, codigo):
        tokens = self.lexer.tokenize(codigo)
        ast = self.parser.parse(tokens)
        for node in ast:
            if isinstance(node, AssignmentNode):
                nome_var = node.var
                valor = self.eval(node.expr)
                self.atribuir(nome_var, valor)
            elif isinstance(node, PrintNode):
                valor = self.eval(node.expr)
                print(valor)

    def eval(self, node):
        if isinstance(node, VariableNode):
            return self.get_variavel(node.var)
        elif isinstance(node, NumberNode):
            return node.value
        elif isinstance(node, StringNode):
            return node.value
        elif isinstance(node, BinaryOpNode):
            left = self.eval(node.left)
            right = self.eval(node.right)
            if node.op == '+':
                return left + right
            elif node.op == '-':
                return left - right
            elif node.op == '*':
                return left * right
            elif node.op == '/':
                return left / right

class Lexer:
    def tokenize(self, codigo):
        tokens = []
        for linha in codigo.splitlines():
            for token in re.split(r'(\s+|[=+\-*/()])', linha):
                if token.strip():
                    tokens.append(token)
        return tokens

class Parser:
    def parse(self, tokens):
        ast = []
        i = 0
        while i < len(tokens):
            if tokens[i] == '=':
                var = tokens[i-1]
                i += 1
                expr = self.parse_expr(tokens, i)
                ast.append(AssignmentNode(var, expr))
            elif tokens[i] == 'print':
                i += 1
                expr = self.parse_expr(tokens, i)
                ast.append(PrintNode(expr))
            i += 1
        return ast

    def parse_expr(self, tokens, i):
        if tokens[i].isdigit():
            return NumberNode(int(tokens[i]))
        elif tokens[i] in ['+', '-', '*', '/']:
            op = tokens[i]
            i += 1
            left = self.parse_expr(tokens, i)
            i += 1
            right = self.parse_expr(tokens, i)
            return BinaryOpNode(op, left, right)
        elif tokens[i].isalpha():
            return VariableNode(tokens[i])
        elif tokens[i].startswith('"') and tokens[i].endswith('"'):
            return StringNode(tokens[i][1:-1])
        else:
            raise Exception("Token inválido")

class Node:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value

class StringNode(Node):
    def __init__(self, value):
        super().__init__('string')
        self.value = value

class AssignmentNode(Node):
    def __init__(self, var, expr):
        super().__init__('assignment')
        self.var = var
        self.expr = expr

class PrintNode(Node):
    def __init__(self, expr):
        super().__init__('print')
        self.expr = expr

class VariableNode(Node):
    def __init__(self, var):
        super().__init__('variable')
        self.var = var

class NumberNode(Node):
    def __init__(self, value):
        super().__init__('number')
        self.value = value

class BinaryOpNode(Node):
    def __init__(self, op, left, right):
        super().__init__('binary_op')
        self.op = op
        self.left = left
        self.right = right

# Exemplo de uso
if __name__==("__main__"):
    lexer = Lexer()
    parser = Parser()
    atribuidor = AtribuidorDeVariaveis(lexer, parser)
    arquivo = open("test.ore", "r")
    for linha in arquivo:
        codigo = arquivo.read()
        atribuidor.executar_codigo(codigo)
        # Descobrir por não atribui número inteiro no arquivo
        print(atribuidor.get_variavel('x'))
        print(atribuidor.get_variavel('nome'))