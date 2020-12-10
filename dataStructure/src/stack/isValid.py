#!/usr/bin/env python3

def isValid( str ):
    print( str );
    dic = {'{': '}',  '[': ']', '(': ')'};
    stack = [];
    for c in str:
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
    str = "{[]}"
    print(isValid( str ));
    s1 = "([)]"
    print(isValid( s1 ));

if __name__ == "__main__":
    main();
