# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 19:34:18 2021

@author: gokul
"""

from stack import Stack

"""
say integer is 10
10//2 = 5 | 10%2 == 0
5//2 = 2  | 5%2 == 1
2//2 = 1  | 2%2 == 0
1//2 = 0  | 1%2 == 1

bin(10) = 1010
"""

def int_to_binary(num):
    bin_stack = Stack()
    while num > 0:
        remainder = num%2
        bin_stack.push(remainder)
        num = num//2
    
    bin_str = ""
    while not bin_stack.is_empty():
        bin_str += str(bin_stack.pop())
    
    return bin_str

print(int_to_binary(4))
print(int_to_binary(242))
