#!/bin/env python3

"""Lists lab:
   1.  create two lists which are different
   2.  compare them for equality
   3.  create a third list which has the same elements as one of the other lists
   4.  verify that Python says they are the same"""

list_one = ['seventeen', 19, 23, 'twenty-nine']
list_two = [17, 19, 23, 29]
list_three = [17, 19, 23, 29]

print(f'\nList one: {list_one}')
print(f'List two: {list_two}')
print(f'List three: {list_three}\n')

if list_one == list_two:
    print('Lists one and two are the same.')
else:
    print('Lists one and two are not the same.')

if list_three == list_two:
    print('List three is the same as list two.\n')
else:
    print('List three is not the same as list two.\n')
