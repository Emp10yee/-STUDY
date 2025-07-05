class Sym:
    OPEN_B=1
    CLOSE_B=2
    PLUS=3
    MINUS=4
    TIMES=5
    DIVIDE=6
    MOD=7
    OPERAND=8

class Expression:
    def __init__(self, expr):
        self.stack=[]
        self.size=100
        self.expr=expr
        self.output=[]
        self.top=-1

    def isEmpty(self):
        return len(self.stack)==0
    
    def isFull(self):
        return len(self.stack) ==self.size
    
    def show_stack(self):
        print(self.stack)

    def push(self, item):
        if self.top < self.size -1:
            self.top +=1
            self.stack.append(item)
            self.show_stack()
        else: print("Stack full")

    def pop(self):
        if self.top >-1:
            self.top -=1
            return self.stack.pop()
        else: print("Stack empty") 

    def eval_postfix(self):
        for sym in self.expr:
            print(sym, end='\t')
            sym_type =self.getSymtype(sym)
            if sym_type ==Sym.OPERAND:
                self.push(float(sym))
            else:
                op2=self.pop()
                op1=self.pop()
                if sym_type ==Sym.PLUS:
                    self.push(op1+op2)
                elif sym_type ==Sym.MINUS:
                    self.push(op1-op2)
                elif sym_type ==Sym.TIMES:
                    self.push(op1*op2)
                elif sym_type ==Sym.DIVIDE:
                    self.push(op1/op2)
                elif sym_type ==Sym.MOD:
                    self.push(op1%op2)
                
        return self.pop()

    def infix_postfix(self):
        for token in self.expr:
            print(token, end ='\t')
            if str(token).isdigit():
                self.output.append(token)
            elif token =='(':
                self.push(token)
            elif token ==')':
                sym=self.pop()
                while sym != '(':
                    self.output.append(sym)
                    sym = self.pop()
            else:
                while self.top > -1 and \
                self.precedence(self.stack[-1]) >= self.precedence(token):
                    sym=self.pop()
                    self.output.append(sym)
                self.push(token)
        while self.top > -1:
            self.output.append(self.pop())
        print()


    def precedence(self, op):
        if op == '(': return 0
        elif op in ['+', '-']: return 1
        elif op in ['*', '/', '%']: return 2

    def getSymtype(self, sym):
        if sym == '(': sym_type = Sym.OPEN_B
        elif sym == ')': sym_type = Sym.CLOSE_B
        elif sym == '+': sym_type = Sym.PLUS 
        elif sym == '-': sym_type = Sym.MINUS
        elif sym == '*': sym_type = Sym.TIMES
        elif sym == '/': sym_type = Sym.DIVIDE
        elif sym == '%': sym_type = Sym.MOD
        else: sym_type = Sym.OPERAND
        return sym_type
 
for expr in ["19 / (30 - 2 * 5 ) - 17 * (26 - 4 )"]:
    expr = expr.split(' ')

    e = Expression(expr)
    print("중위 수식=", expr)
    e.infix_postfix()
    print("변환 후위 수식=", e.output)
    e. stack=[]
    e.expr = e.output
    print("후위 수식 계산 값 =", e.eval_postfix())
    print()