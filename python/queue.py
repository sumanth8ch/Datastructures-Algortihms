"""Queue() creates a new queue that is empty. 
enqueue(item) adds a new item to the rear of the queue. 
dequeue() removes the front item from the queue. 
isEmpty() tests to see whether the queue is empty. 
size() returns the number of items in the queue."""

class Queue:
    
    def __init__(self):
        self.qitems = []

    def size(self):
        return len(self.qitems)
     
    def enqueue(self,value):
        self.qitems.insert(0,value)
        
    def dequeue(self):
        return self.qitems.pop()
    
    def isEmpty(self):
        return self.qitems == []
    
    
if __name__ == '__main__':
    
    newq = Queue()
    
    print(newq.isEmpty()) 
    
    newq.enqueue(1)
    newq.enqueue('stack')
    newq.enqueue(8673)
    
    print('The length of queue is '+str(newq.size()))
    
    print(str(newq.dequeue()) +' is removed from queue')
    
    print('The length of queue is '+str(newq.size()))
