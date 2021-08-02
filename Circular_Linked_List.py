# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 12:37:36 2021

@author: gokul
"""

# Python program to demonstrate working of circular linked list
 
# Structure for a Node
class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next 
    

class CircularLinkedList: 
    # Constructor to create a empty circular linked list
    def __init__(self):
        self.head = None
     
    # Function to insert a node at the beginning of a circular linked list 
    def prepend(self, val):
        if not self.head:
            node = Node(val)
            self.head = node
            self.head.next = self.head
        else:
            node = Node(val, self.head)
            ele = self.head
            while ele.next != self.head:
                ele = ele.next
            ele.next = node 
            #Only difference between append and prepend is new node becomes head
            self.head = node
        
    # Function to insert a node at the end of a circular linked list 
    def append(self, val):
        if not self.head:
            node = Node(val)
            self.head = node
            self.head.next = self.head
        else:
            node = Node(val, self.head)
            ele = self.head
            while ele.next != self.head:
                ele = ele.next
            #If linked list is not None then set the next of last node to new node
            #And the next of new node corresponds to head
            ele.next = node
     
    def __len__(self):
        ele = self.head
        count = 0
        while ele:
            count += 1
            if ele.next == self.head:
                break
            ele = ele.next
        return count            
        
    # Function to print nodes in a given circular linked list
    def printList(self):
        ele = self.head
        cllstr = ''
        while ele:
            cllstr += str(ele.val)+'-->'
            if ele.next == self.head:
                break
            ele = ele.next
        print(cllstr)
    
    #Function to split the circular linked list into two based on midpoint
    def split_list(self):
        size = len(self)
        
        if size == 0:
            return None
        elif size == 1:
            return self.head
        else:
            mid = size//2
            prev = None
            cur = self.head
            count = 0
            while cur and count < mid:
                prev = cur
                cur = cur.next
                count += 1
            prev.next = self.head
            
            split_cllist = CircularLinkedList()
            while cur != self.head:
                split_cllist.append(cur.val)
                cur = cur.next

            print("Lists after splitting:")
            self.printList()
            split_cllist.printList()            
        
    #Function to remove an element from the list based on value    
    def remove(self, val):
        if self.head.next == self.head and self.head.val == val:
            self.head = None        
        else:
            if self.head.val == val:
                new_head = self.head.next
                ele = self.head
                while ele.next != self.head:
                    ele = ele.next
                ele.next = new_head
                self.head = new_head
            else:
                ele = self.head
                while ele.next != self.head:
                    list_val = ele.next.val
                    if list_val == val:
                        ele.next = ele.next.next
                        break
                    ele = ele.next                                           


if __name__ == '__main__':
    # Initialize list as empty
    cllist = CircularLinkedList()
     
    # Created linked list will be 11->2->56->12
    cllist.append(12)
    cllist.append(56)
    #cllist.append(2)
    cllist.prepend(11)
    cllist.prepend('XD')
    cllist.prepend('Century')
    cllist.append(['a', 'b', 'c'])
    
    
    cllist.remove('Century')
    cllist.remove(56)
    cllist.remove(['a', 'b', 'c'])
    cllist.remove(12)
    cllist.remove(11)
    cllist.remove(19)
    cllist.remove('XD')
    
    print ("Contents of circular Linked List")
    cllist.printList()
    print('\n')
    
    print("Length of the list:")
    print(len(cllist))
    print('\n')
    
    cllist.split_list()