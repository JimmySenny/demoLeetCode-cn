#!/usr/bin/env python3
class Solution:
    def isValid( s ):
        print( str );
        dic = {'{': '}',  '[': ']', '(': ')'};
        stack = [];
        for c in s:
            if c in dic:
                print(c);
                stack.append(c);
                print( "append", end='')
                print( stack );
            else:
                if len(stack) == 0:
                    return False;
                else:
                    top = stack.pop();
                    print( "pop", end='')
                    print( stack );
                    if c != dic[top]:
                        return False;
        return not stack;

def main():
    s = Solution()
    str = "{[]}"
    print(s.isValid( str ));
    s1 = "([)]"
    print(s.isValid( s1 ));

if __name__ == "__main__":
    main();
