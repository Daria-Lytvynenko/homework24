import re
from collections import deque
if __name__ == '__main__':
    #Task 1 Write a program that reads in a sequence of characters and prints them in reverse order, using
    #your implementation of Stack.
    stack=deque()
    for i in range(1, 8):
        stack.append(i)
    while len(stack) >= 1:
        print(stack.pop())
    #Task 3 Extend the Stack to include a method called get_from_stack that searches and returns an
    #element e from a stack.Any  other element must remain on the stack respecting their order.Consider
    #the case in which the element is not found - raise ValueError with proper info Message

    stack = []
    stack2 = []
    def get_from_stack(val):
        stack.append('a')
        stack.append('b')
        stack.append('g')
        stack.append('c')
        stack.append('d')
        while len(stack)>=1:
            x=stack.pop()
            try:
                if x==val:
                    print(x)
                elif x!=val:
                    stack2.append(x)
            except ValueError:
                print('Element nor found')

        return (f"New stack: {stack2[::-1]} ")
    print(get_from_stack('g'))



   #Task 2 Write a program that reads in a sequence of characters, and determines whether it's parentheses, ' \
    #braces, and curly brackets are "balanced."
    expr= input("Input some expression:")
    def balance(expr):
        token_list=re.split('([^A-z])', expr)
        a = token_list.count('{')
        b = token_list.count('}')
        c = token_list.count('(')
        d = token_list.count(')')
        e = token_list.count('[')
        f = token_list.count(']')
        if a==b and c==d and e==f:
            return (f"parentheses are balanced")
        else:
            return (f"parentheses are not balanced")
    print(balance(expr))
