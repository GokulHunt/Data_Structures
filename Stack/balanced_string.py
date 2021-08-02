# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 19:05:39 2021

@author: gokul
"""

from stack import Stack

"""Function to find if any two brackets are matched"""
def is_pair(str1, str2):
    if str1+str2 in ('()', '{}', '[]'):
        return True
    return False


"""Function to find if a string has proper opening and closure of brackets"""
def is_balanced_string(string):
    str_stack = Stack()
    flag = False
    for ip in string:
        if ip in ('(', '{', '['):
            str_stack.push(ip)
        else:
            if str_stack.is_empty():
                flag = False
                break
            else:
                out = str_stack.pop()
                if not is_pair(out, ip):
                    flag = False
                    break
                else:
                    flag = True
        #print(str_stack.get_stack(), flag)
    
    if str_stack.is_empty() == True:
        return flag
    return flag


is_balanced_string('{{{{[]()}}}}]()')

    
    