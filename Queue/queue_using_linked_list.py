# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 09:36:23 2021

@author: gokul
"""

"""
Implementation of Queue Data Structure using Linked List
"""

class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next


class Queue:
    #Constructor to create an empty queue
    def __init__(self):
        self.front = None
        self.rear = None
    
    #Function to add elements at the end of the queue
    def enqueue(self, val):
        if self.rear == None:
            node = Node(val)
            self.front = node
            self.rear = node
        else:
            node = Node(val)
            self.rear.next = node
            self.rear = self.rear.next
    
    #Funtion to remove the first element in the queue
    def dequeue(self):
        if self.front == None:
            return "Empty Queue"
        else:
            out = self.front.val
            if  self.front == self.rear:
                self.rear = self.rear.next
            self.front = self.front.next
            return out
    
    #Function to return the size of the queue    
    def __len__(self):
        count = 0
        ele = self.front
        while ele:
            count += 1
            ele = ele.next
        return count
    
    #To check whether a queue is empty
    def is_empty(self):
        return self.front is None
    
    #Print function to print out the queue
    def __str__(self):
        queue_str = ''
        ele = self.front
        while ele:
            if ele == self.rear:
                queue_str += 'rear('+str(ele.val)+')'
            elif ele == self.front:
                queue_str += 'front('+str(ele.val)+')-->'
            else:
                queue_str += str(ele.val)+'-->'
            
            ele = ele.next
        return queue_str
    
    #Getter function to get the front element
    def get_front(self):
        return self.front.val
    
    #Getter function to get the rear element
    def get_rear(self):
        return self.rear.val
    
    
    
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



            