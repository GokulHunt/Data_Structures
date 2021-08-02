# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 19:34:18 2021

@author: gokul
"""

from stack import Stack

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
