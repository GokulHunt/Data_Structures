# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 10:31:19 2021

@author: gokul
"""

"""
Implementation of Queue Data Structure using Python
First-In-First-Out principle
"""

class Queue:
    #Constructor to create an empty Queue
    def __init__(self):
        self.items = []
    
    #function for pushing an element into the Queue
    def enqueue(self, val):
        self.items.insert(0, val)
        
    #function for popping up the fore most element from the queue
    def dequeue(self):
        front = self.items.pop()
        return front
    
    #function to check whether the Queue is empty
    def is_empty(self):
        return self.items == []
    
    #this function returns the entire Queue
    def get_queue(self):
        return self.items
    
    #Getter function to get the front element
    def get_front(self):
        return self.items[-1]
    
    #Getter function to get the rear element
    def get_rear(self):
        return self.items[0]
    
    #Function to override print() to display the queue
    def __str__(self):
        return str(self.items)
    
    #Function to override len() to print out the length
    def __len__(self):
        return len(self.items)
    
    
if __name__ == '__main__':
    q = Queue()
    q.enqueue(5)
    q.enqueue('Blitzkreig')
    q.enqueue('IamLegend')
    q.enqueue('Will Smith')
    q.enqueue('#')
    q.enqueue(1000)
    print(q)
    len(q)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    q.is_empty()
    q.enqueue('Done!!')
    q.enqueue(True)
    print(q)
    print(q.get_front())
    print(q.get_rear())