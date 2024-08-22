class Token:
    def __init__(self,tp,value=None):
        self.type=tp
        self.value=value
    def __repr__(self) -> str:
        return "<Token "+self.type+("" if self.value==None else ":"+str(self.value))+">"
NUMBERS="0123456789."
class Lexer:
    def __init__(self):
        self.txt=""
        self.char=None
        self.pos=0
    def next(self):
        self.pos+=1
        if self.pos<len(self.txt):
            self.char=self.txt[self.pos]
        else:
            self.char=None
    def tokenizer(self,txt):
        self.txt=txt
        self.pos=-1
        self.next()
        ret=[]
        while self.char!=None:
            if self.char in NUMBERS:
                st=""
                f=False
                while self.char!=None and self.char in NUMBERS:
                    if self.char==".":
                        if f:
                            return []
                        else:
                            f=True
                    st+=self.char
                    self.next()
                ret.append(Token("value",float(st) if f else int(st)))
                continue
            elif self.char=='"':
                self.next()
                st=""
                while self.char!=None: 
                    if self.char=='"':
                        self.next()
                        break
                    st+=self.char
                    self.next()
                ret.append(Token("value",st))
            elif self.char=="'":
                self.next()
                st=""
                while self.char!=None: 
                    if self.char=="'":
                        self.next()
                        break
                    st+=self.char
                    self.next()
                ret.append(Token("value",st))
            elif self.char=="+":
                ret.append(Token("+"))
            elif self.char=="-":
                ret.append(Token("-"))
            elif self.char=="*":
                ret.append(Token("*"))
            elif self.char=="/":
                ret.append(Token("/"))
            self.next()
        return ret
if __name__=="__main__":
    l=Lexer()
    t=l.tokenizer("1+1")
    print(t)
    t=l.tokenizer('"aaa"')
    print(t)