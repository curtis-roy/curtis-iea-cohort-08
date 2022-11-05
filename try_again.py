#!/bin/env python3

""" If I remember correctly, this was the gist:
    Look at a list of 3 items.  Ignore the first item (position 0).
    If the item at position 1 == APPLY, then print the last item in the list.
    Change the last item in the list, then print again with the new one."""

def tryagain():
    sentence = []
    for i in elements:
        if elements[1] == "APPLY":
            sentence.append(elements[-1])
            print(sentence)

elements = [0, 'APPLY', 'Hey']
values = ['Hey', 'there', '!']

tryagain()

# JR off the cuff idea print(fields[-1] if fields[1] == "APPLY" else "")