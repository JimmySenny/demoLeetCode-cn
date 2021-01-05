#!/usr/bin/env python3

class Solution:
#    def evalRPN(self, tokens: List[str]) -> int:
    def evalRPN(self, tokens):
        stack = []
        i = 0
        tmp = 0;
        tmp2 = 0;
        for i in range(len(tokens)):
            if tokens[i] == "+":
                stack.append(stack.pop() + stack.pop())
                pass
            elif tokens[i] == "-":
                tmp = stack.pop()
                stack.append(stack.pop() - tmp )
                pass
            elif tokens[i] == "*":
                stack.append(stack.pop()*stack.pop())
                pass
            elif tokens[i] == "/":
                tmp = stack.pop()
                stack.append(int(stack.pop() / tmp))
                pass
            else:
                stack.append(int(tokens[i]))
            print("i,token[i],stack",i,tokens[i],stack)
        return stack.pop()

def main():
    s = Solution();
    t = ["2", "1", "+", "3", "*"]
    print(s.evalRPN(t));
    t = ["4","13","5","/","+"]
    print(s.evalRPN(t));
    t = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(s.evalRPN(t));


if __name__ == '__main__':
    main()
