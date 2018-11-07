#!/usr/bin/env python3

import operator
import math

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '!': math.factorial,
}

def percent(arg1, arg2, operation):
    arg2 = arg1 * arg2 / 100
    function = operators[operation]
    ans = function(arg1, arg2)
    return ans

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            if token == '!':
                function = operators[token]
                arg1 = stack.pop()
                result = function(arg1)
                stack.append(result)
            else:
                function = operators[token]
                arg2 = stack.pop()
                arg1 = stack.pop()
                result = function(arg1, arg2)
                stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)

if __name__ == '__main__':
    main()
