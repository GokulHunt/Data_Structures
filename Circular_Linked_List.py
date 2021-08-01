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
     
     
    # Function to print nodes in a given circular linked list
    def printList(self):
        ele = self.head
        cllstr = ''
        while ele:
            if ele.next != self.head:
                cllstr += str(ele.val)+'-->'
            else:
                cllstr += str(ele.val)
                break
            ele = ele.next
        print(cllstr)
 
 
# Driver program to test above function
 
# Initialize list as empty
cllist = CircularLinkedList()
 
# Created linked list will be 11->2->56->12
cllist.append(12)
cllist.append(56)
cllist.append(2)
cllist.prepend(11)
 
print ("Contents of circular Linked List")
cllist.printList()