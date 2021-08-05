# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 16:22:20 2021

@author: gokul
"""

#Implementation of Stack Data Structure using Python
class Stack:
    #Constructor to create an empty Stack
    def __init__(self):
        self.items = []
    
    #function for pushing an element into the stack
    def push(self, val):
        self.items.append(val)
        
    #function for popping up the top-most elemet in the stack
    def pop(self):
        top = self.items.pop()
        return top
    
    #this function returns the top element without actually dropping it
    def peek(self):
        return self.items[-1]
    
    #function to check whether the stack is empty
    def is_empty(self):
        return self.items == []
    
    #this function returns the entire stack
    def get_stack(self):
        return self.items
    
    #this function prints out the stack elements starting from the top element
    def __str__(self):
        this_stack = self.get_stack()
        stack_items = ''
        for i in range(len(this_stack)-1, -1,  -1):
            if i != 0:
                stack_items += str(this_stack[i])+',\n'
            else:
                stack_items += str(this_stack[i])+'\n'
            
        return "[\n"+stack_items+"]"
        
if __name__ == '__main__':    
    my_stack = Stack()
    my_stack.push(1)
    my_stack.push('Gokul')
    my_stack.push('SuperStar')
    my_stack.push('#')
    my_stack.push('Aurora')
    my_stack.push(100)
    my_stack.pop()
    print(my_stack.peek())
    print(my_stack.is_empty())
    print(my_stack.get_stack())
    print(my_stack)
