class mystack:
    def __init__(self,capacity):
        self.capacity = capacity
        self.a=[]
        self.top = -1
    def is_empty(self):
        return len(self.a)==0
    def is_full(self):
        return len(self.a)==self.capacity
    def pop(self):
        if not self.is_empty():
            return self.a.pop()
    def push(self,element):
        if not self.is_full():
            self.a.append(element)
    def eval_postfix(self,expression):
        for i in expression:
            if i.isdigit():
                self.push(i)
            else:
                var1 = self.pop()
                var2 = self.pop()
                var3 = str(eval(var1+i+var2))
                self.push(var3)
        return int(str(self.pop()))

exp = "231*+9-"
l = len(exp)
obj = mystack(l)
result = obj.eval_postfix(exp)
print(result)