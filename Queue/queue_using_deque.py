# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 15:30:03 2021

@author: gokul
"""

from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self, val):
        self.queue.appendleft(val)
        
    def dequeue(self):
        return self.queue.pop()
        
    def __len__(self):
        return len(self.queue)
    
    def __str__(self):
        queue_str = ''
        if len(self.queue) == 1:
            return str(self.queue[0])
        else:
            for i in range(len(self.queue)-1, -1, -1):
                if i == 0:
                    queue_str += str(self.queue[i])
                else:
                    queue_str += str(self.queue[i])+'-->'
        return queue_str
    
    
if __name__ == '__main__':
    q = Queue()
    q.enqueue(5)
    q.enqueue('Blitzkreig')
    q.enqueue('IamLegend')
    q.enqueue('Will Smith')
    q.enqueue('#')
    q.enqueue(1000)
    print(q)