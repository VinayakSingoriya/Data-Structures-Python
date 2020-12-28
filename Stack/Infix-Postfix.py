class Conversion():
    def __init__(self):
        self.top = -1
        self.array = list()
        self.result = list()
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}

    def isEmpty(self):
        return True if self.top == -1 else False  

    def peek(self):
        return self.array[-1]

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"  

    def push(self, op):
        self.top +=1
        self.array.append(op) 

    def isoperand(self, ch):
        return ch.isalpha() 

    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()] 
            return True if a <= b else False
        except KeyError:
            return False



    def infixToPostfix(self, expression): 
        for i in expression:
            if self.isoperand(i):
                self.result.append(i)

            elif i == '(':
                self.push(i)

            elif i == ')':
                while((not self.isEmpty()) and self.peek()!='('):
                    a = self.pop()
                    self.result.append(a)
                if(not self.isEmpty() and self.peek()!='('):
                    return -1
                else:
                    self.pop()

            else:
                while(not self.isEmpty() and self.notGreater(i)):
                    self.result.append(self.pop())
                self.push(i)  

        while not self.isEmpty():
            self.result.append(self.pop())  

        print("".join(self.result))


exp = "a+b*(c^d-e)^(f+g*h)-i"
obj = Conversion()
obj.infixToPostfix(exp)                                    
