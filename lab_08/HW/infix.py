#한국역사학과 20180269 천성규
from stacks import Stack

class Infix:
    OPS = "+", "-", "*", "/"
    def __init__(self, expr):
        (*self.expr,) = expr
        
    def translate_postfix(self):
        stack = Stack(len(self.expr))
        
        list_ = []
        for token in self.expr:
            if token == '(' or token in Infix.OPS:
                stack.push(token)
                continue
            
            if token != ')':
                list_.append(token)
                continue
        
            while not stack.is_empty() and stack.peek() != '(':
                list_.append(stack.peek())
                stack.pop()

            stack.pop()
            
            while not stack.is_empty() and stack.peek() != '(':
                list_.append(stack.peek())
                stack.pop()

        while not stack.is_empty():
            list_.append(stack.peek())
            stack.pop()
            
        return "".join(list_)
    
    def translate_prefix(self):
        stack = Stack(len(self.expr))
        ret = []
        
        for token in self.expr:
            if token == "(" or token in Infix.OPS:
                stack.push(token)
                continue
            
            if token != ")":
                ret.append(token)
                continue
            
            while not stack.is_empty() and stack.peek() != "(":
                op = stack.peek()
                stack.pop()
                op1 = ret.pop()
                op2 = ret.pop()
                
                tmp = op + op2 + op1
                ret.append(tmp)
            
            stack.pop()
            
            while not stack.is_empty() and stack.peek() != "(":
                op = stack.peek()
                stack.pop()
                op1 = ret.pop()
                op2 = ret.pop()
                
                tmp = op + op2 + op1
                ret.append(tmp)
        
        while not stack.is_empty():
            op = stack.peek()
            stack.pop()
            op1 = ret.pop()
            op2 = ret.pop()
            
            tmp = op + op2 + op1
            ret.append(tmp)
        
        return "".join(ret)
    
    def postfix_to_infix(self, expr):
        s = Stack(len(expr))
        
        for i in expr:
            if i in Infix.OPS:
                op1 = s.peek()
                s.pop()
                op2 = s.peek()
                s.pop()
                s.push("(" + op2 + i + op1 + ")")
            else:
                s.push(i)

        return s.peek()
    
    def prefix_to_infix(self, expr):
        s = Stack(len(expr))
        
        i = len(expr) - 1
        while i >= 0:
            if expr[i] not in Infix.OPS:
                s.push(expr[i])
                i -= 1
            else:
                op1 = s.peek()
                s.pop()
                op2 = s.peek()
                s.pop()
                s.push("(" + op1 + expr[i] + op2 + ")")
                i -= 1
        ret = s.peek()
        return ret
    
if __name__ == "__main__":
    expr = "a * ( b + c ) * d"
    print(f"Infix =\n{expr}")
    infix = Infix(expr.split())
    postfix = infix.translate_postfix()
    print(f"Postfixt =\n{postfix}")
    
    postfix = infix.postfix_to_infix(postfix)
    print(f"Postfixt =\n{postfix}")
    
    prefix = infix.translate_prefix()
    print(f"Prefix =\n{prefix}")
    
    prefix = infix.prefix_to_infix(prefix)
    print(f"Prefix =\n{prefix}")
