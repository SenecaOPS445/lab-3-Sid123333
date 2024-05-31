#!/usr/bin/env python3
'''Lab 3 Inv 2 function operate '''
#Author ID= Siddhartha Shrestha
#Student ID = 160706222

def operate(number1, number2, operator):
    if operator == 'add':
        a = number1 + number2
    elif operator == 'subtract':
        a = number1 - number2
    elif operator == 'multiply':
        a = number1 * number2
    else:
        a = 'Error: function operator can be "add", "subtract", or "multiply"'
    return a

if __name__ == '__main__':
    print(operate(10, 5, 'add'))
    print(operate(10, 5, 'subtract'))
    print(operate(10, 5, 'multiply'))
    print(operate(10, 5, 'divide'))