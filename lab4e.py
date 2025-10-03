#!/usr/bin/env python3
# Author ID: vpatel278, 166249219

def is_digits(sobj):
    # Return False for empty strings (no digits present)
    if sobj == '':
        return False
    # Check each character: must be between '0' and '9'
    for ch in sobj:
        if ch < '0' or ch > '9':
            return False
    return True

if __name__ == '__main__':
    test_list = ['x3058','3058','8503x','8503']
    for item in test_list:
        if is_digits(item):
            print(item, 'is an integer.')
        else:
            print(item, 'is not an integer.')

