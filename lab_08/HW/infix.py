#한국역사학과 20180269 천성규
from stacks import Stack

class Infix:
    def __init__(self, expr):
        (*self.expr,) = expr
        
    def translate_postfix(self):
        stack = Stack(len(self.expr))
        
        list_ = []
        for token in self.expr:
            if token.isalpha():
                list_.append(token)
            elif token == '(':
                stack.push(token)
            elif token == ')':
                while((not stack.is_empty()) and stack.peek() != '('):
                    a = stack.peek()
                    list_.append(a)
                    stack.pop()
                stack.pop()
            else:
                while((not stack.is_empty()) and stack.peek() != '('):
                    list_.append(stack.peek())
                    stack.pop()
                stack.push(token)
            

        while not stack.is_empty():
            if stack.peek() == '(':
                stack.pop()
            list_.append(stack.peek())
            stack.pop()

        return "".join(list_)
    
if __name__ == "__main__":
    expr = "a*(b+c)*d"
    infix = Infix(expr)
    postfix = infix.translate_postfix()
    print(postfix)