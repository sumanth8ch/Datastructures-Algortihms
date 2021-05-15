"""The stack operations are given below:

Stack(): creates a new stack that is empty.

push(item) : adds a new item to the top of the stack. 

pop() : removes the top item from the stack.

peek() : returns the top item from the stack but does not remove it. 

isEmpty() : tests to see whether the stack is empty. 

size() : returns the number of items on the stack. """


class Stack:
    
    def __init__(self):
        self.stackitems = []

    def size(self):
        return len(self.stackitems)
     
    def push(self,value):
        self.stackitems.append(value)
        
    def pop(self):
        return self.stackitems.pop()
    
    def peek(self):
        return self.stackitems[len(self.stackitems)-1]
    
    def isEmpty(self):
        return self.stackitems == []
    
    
if __name__ == '__main__':
    
    newstack = Stack()
    
    print(newstack.isEmpty()) 
    
    newstack.push(1)
    newstack.push('stack')
    newstack.push(8673)
    
    print('The length of stack is '+str(newstack.size()))
    
    print(str(newstack.peek()) +' is peeked')
    
    print('The length of stack is '+str(newstack.size()))
    
    print(str(newstack.pop()) +' is popped out')
    
    print('The length of stack is '+str(newstack.size()))
    
   
    
    
    
    
    
    
