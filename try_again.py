#!/bin/env python3

""" If I remember correctly, this was the gist:
    Look at a list of 3 items.  Ignore the first item.
    If the middle item == APPLY, then print the last item in the list.
    Change the last item in the list, then print again with the new one."""

def tryagain():
    del elements[0] # Get rid of item at pos 0 since we're not using it anyway
    empty = [] # an empty list to put things into
    if elements[0] == 'APPLY': # meeting the specified condition
        for item in elements:
            empty.append(elements[-1]) # add last item in elements to empty list
            elements[-1] = values[0] # set last item in elements to new value from values
    print(empty)

elements = [0, 'APPLY', 'Hey']
values = ['there']

tryagain()
