#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(s):
    # first_five(s): return the first 5 characters of s
    s = str(s)
    return s[:5]

def last_seven(s):
    # last_seven(s): return the last 7 characters of s
    s = str(s)
    return s[-7:]

def middle_number(n):
    # middle_number(n): accept a number, return characters 2 and 3 as a string
    s = str(n)
    return s[1:3]

def first_three_last_three(a, b):
    # first_three_last_three(a, b): first 3 chars of a + last 3 chars of b
    a = str(a)
    b = str(b)
    return a[:3] + b[-3:]

if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))
