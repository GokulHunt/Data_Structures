# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 07:58:24 2021

@author: gokul
"""

class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next
    
    
    
class linked_list:
    def __init__(self):
        self.head = None
    
    
    def __str__(self):
        if self.head == None:
            return("Linked List is empty")        
        else:
            ele =  self.head            
            llstr = ''            
            while ele:
                llstr += str(ele.val)+'-->' if ele.next else str(ele.val)
                ele = ele.next                
            return(llstr)
    
    
    def __len__(self):
        count = 0
        ele = self.head
        while ele:
            count += 1
            ele = ele.next
            
        return count
    
    
    def insert_at_beginning(self, val):
        node = Node(val, self.head)
        self.head = node
    
    
    def insert_at_end(self, val):
        ele = self.head
        if self.head is None:
            node = Node(val, None)
            self.head = node            
        else:
            while ele.next:
                ele = ele.next            
            ele.next = Node(val, None)
         
            
    def insert_at_position(self, idx, val):
        if idx < 0 or idx > self.__len__():
            raise IndexError("Invalid Index")
        else:
            if idx == 0:
                self.insert_at_beginning(val)
                return
            
            count = 0
            ele = self.head
            while ele:
                if count == idx - 1:
                    node = Node(val, ele.next)
                    ele.next = node
                    break
                
                ele = ele.next
                count += 1


    def insert_after_value(self, val_after, val_to_insert):
        ele = self.head
        while ele:
            if ele.val == val_after:
                node = Node(val_to_insert, ele.next)
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
                break
            
            ele = ele.next
            count += 1
    
    
    def remove_by_value(self, val):
        ele = self.head
        while ele.next:
            list_val = ele.next.val
            if list_val == val:
               ele.next = ele.next.next
            
            ele = ele.next
            

        
if __name__ == '__main__':
    l = linked_list()
    l.insert_at_beginning(5)
    l.insert_at_beginning(625)
    l.insert_at_end(':P')
    l.insert_at_position(3, "^v^")
    l.insert_at_position(4, ':D')
    l.insert_multiple_values(['a','b', 100, 'Century'])
    l.remove_at_position(5)
    l.remove_at_position(4)
    print(l)
    print(len(l))
    l.insert_after_value(':P', 'XD')
    l.remove_by_value(100)
    l.remove_by_value(':P')    
    print(l)
