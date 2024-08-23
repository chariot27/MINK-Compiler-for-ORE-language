class Token:
    def __init__(self,type="",value=None):
        self.type=type
        self.value=value
    def __repr__(self):
        return "<Token "+str(self.type)+">" if self.value==None else "<Token "+str(self.type)+":"+str(self.value)+">"
numbers="0123456789"
point="."
plus="+"
minus="-"
multiply="*"
divade="/"
class Lexer:
    def __init__(self):
        self.pos=0
        self.txt=""
        self.char=""
    def __call__(self,txt):
        self.txt=txt
        self.pos=-1
        self.char=None
        self.next()
        tokens=[]
        while self.char!=None:
            self.skip_write_places()
            if self.char in numbers+point:
                tok=Token("Value")
                n=self.char+""
                self.next()
                ok=False
                while self.char!=None and self.char in numbers+point:
                    if len(n)==1 and n==".":
                        ok=True
                    if self.char==".":
                        if ok:
                            pass
                        ok=True
                    n+=self.char
                    self.next()
                if ok:
                    tok.value=int(n)
                else:
                    tok.value=float(n)
                tokens.append(tok)
                continue
            elif self.char==plus:
                tokens.append(Token("+"))
            elif self.char==minus:
                tokens.append(Token("-"))
            elif self.char==multiply:
                tokens.append(Token("*"))
            elif self.char==divade:
                tokens.append(Token("/"))
            self.next()
        return tokens
    def skip_write_places(self):
        while self.char!=None and self.char==" ":
            self.next()
    def next(self):
        self.pos+=1
        if self.pos>=len(self.txt):
            self.char=None
        else:
            self.char=self.txt[self.pos]
class Node:
    def __init__(self,type="",value=None):
        self.type=type
        self.value=value
    def __repr__(self):
        return "<Node "+str(self.type)+">" if self.value==None else "<Node "+str(self.type)+":"+str(self.value)+">"
class Parser:
    def __init__(self):
        self.tok_pos=0
        self.tok=None
        self.tokens=[]
    def expr(self):
        re=self.term()
        return re
    def term(self):
        re=self.factor()
        if self.tok!=None:
            if self.tok.type=="+":
                self.nextTok()
                re=Node("+",[re,self.term()])
            elif self.tok.type=="-":
                self.nextTok()
                re=Node("-",[re,self.term()])
            elif self.tok.type=="*":
                self.nextTok()
                re=Node("*",[re,self.term()])
            elif self.tok.type=="/":
                self.nextTok()
                re=Node("/",[re,self.term()])
        return re
    def factor(self):
        tok=self.tok
        if self.tok.type=="Value":
            self.nextTok()
            return Node("Value",tok.value)
        elif self.tok.type=="-":
            self.nextTok()
            return Node("inverseNumber",tok.value)
    def __call__(self,tokens):
        self.tok_pos=-1
        self.tokens=tokens
        self.tok=None
        self.nextTok()
        return self.expr()
    def nextTok(self):
        self.tok_pos+=1
        if self.tok_pos>=len(self.tokens):
            self.tok=None
        else:
            self.tok=self.tokens[self.tok_pos]
if __name__==("__main__"):
    l=Lexer()
    p=Parser()
    toks=l("10-1")
    print(toks)
    nodes=p(toks)
    print(nodes)
