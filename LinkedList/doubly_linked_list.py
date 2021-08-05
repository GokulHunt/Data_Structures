# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 09:44:11 2021

@author: gokul
"""

class Node:
    def __init__(self, val = None, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev
    
    
    
class doubly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
    
    
    def print_forward(self):
        if self.head == None:
            return("Linked List is empty")        
        else:
            ele =  self.head            
            llstr = ''            
            while ele:
                llstr += str(ele.val)+'-->' if ele.next else str(ele.val)
                ele = ele.next                
            print(llstr)
    
    
    def print_backward(self):
        if self.tail == None:
            return("Linked List is empty")        
        else:
            ele =  self.tail            
            llstr = ''            
            while ele:
                llstr += str(ele.val)+'-->' if ele.prev else str(ele.val)
                ele = ele.prev                
            print(llstr)
        
        
    def __len__(self):
        count = 0
        ele = self.head
        while ele:
            count += 1
            ele = ele.next
            
        return count
    
    
    def insert_at_beginning(self, val):
        node = Node(val, self.head, None)
        self.head = node
    
        ele = self.head
        while ele.next:
            ele.next.prev = ele
            ele = ele.next
        self.tail = ele
                
        
    def insert_at_end(self, val):
        ele = self.tail
        if self.tail is None:
            node = Node(val, None, None)
            self.head = node   
            self.tail = node
        else:
            ele.next = Node(val, None, ele)
            self.tail = ele.next
         
            
    def insert_at_position(self, idx, val):
        if idx < 0 or idx > self.__len__():
            raise IndexError("Invalid Index")
            
        else:
            if idx == 0:
                self.insert_at_beginning(val)
                return
            elif idx == self.__len__():
                self.insert_at_end(val)
                return
            
            count = 0
            ele = self.head
            while ele:
                if count == idx - 1:
                    node = Node(val, ele.next, ele)
                    ele.next = node
                    break
                
                ele = ele.next
                count += 1


    def insert_after_value(self, val_after, val_to_insert):
        ele = self.head
        while ele:
            if ele.val == val_after:
                node = Node(val_to_insert, ele.next, ele)
                ele.next = node
                break
            ele = ele.next


    def insert_multiple_values(self, list_of_values):
        for val in list_of_values:
            self.insert_at_end(val)
      
            
    def remove_at_position(self, idx):
        if idx < 0 or idx >= self.__len__():
            raise IndexError("Invalid Index")
        else:
            if idx == 0:
                self.head = self.head.next
                return
            
        count = 0
        ele = self.head
        while ele:
            if count == idx - 1:
                ele.next = ele.next.next
                ele.next.prev = ele
                break
            
            ele = ele.next
            count += 1
    
    
    def remove_by_value(self, val):
        ele = self.head
        while ele.next:
            list_val = ele.next.val
            if list_val == val:
               ele.next = ele.next.next
               ele.next.prev = ele
               break
            
            ele = ele.next
            

        
if __name__ == '__main__':
    dl = doubly_linked_list()
    dl.insert_at_beginning(5)
    dl.insert_at_beginning(625)
    dl.insert_at_end(225)
    dl.insert_at_position(3, "^v^")
    dl.insert_multiple_values(['a','b', 100, 'Century'])
    dl.insert_after_value(225, 'XD')
    dl.print_forward()
    dl.print_backward()  
    
    dl.remove_at_position(5)
    dl.remove_at_position(4)
    dl.print_forward()
    dl.print_backward() 
    
    dl.remove_by_value(100)
    dl.remove_by_value(225)    
    dl.print_forward()
    dl.print_backward() 
    print(len(dl))
    