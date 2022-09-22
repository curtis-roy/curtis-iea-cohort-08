#!/bin/env python3

""" Use this to copy/paste stuff from other scripts that are
    not working as expected, or as a placeholder to preserve
    something that I haven't managed to break...yet. """

def calculate(val1, val2, operator):
    """ Docstring for lab calculator. """
    if operator == '+':
        calculation = val1 + val2
    if operator == '-':
        calculation = val1 - val2
    if operator == '*':
        calculation = val1 * val2
    if operator == '/':
        try:
            calculation = val1 / val2
        except ZeroDivisionError:
            print('Cannot divde by zero.')
    return calculation

print(calculate(2, 0, '-'))

################################################################################

start_number = int(input('Enter start number: '))

def collatz(start_number):
    while start_number > 1:
        print(start_number, end = ' ')
        if start_number % 2: # odd number
            start_number = 3 * start_number + 1
        else: # even number
            start_number = start_number // 2
    print(1)

print('Collatz Conjecture sequence: ')

collatz(start_number)
