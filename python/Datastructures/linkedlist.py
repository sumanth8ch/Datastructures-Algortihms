""" LinkedList() creates a new list that is empty.   
    add(item) adds a new item to the list.
    remove(item) removes the item from the list.
    search(item) searches for the item in the list.
    isEmpty() tests to see whether the list is empty.
    size() returns the number of items in the list. 
    append(item) adds a new item to the end of the list.
    printlist() prints the list.
 """

class Node:
     
    def __init__(self,value):
        self.ndata = value
        self.nextnode = None
        
    def getValue(self):
        return self.ndata
    
    def setValue(self,newvalue):
        self.ndata = newvalue
        
    def getNext(self):
        return self.nextnode
    
    def setNext(self,newnextnode):
        self.nextnode = newnextnode
        
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head == None
    
    def size(self):
        curnode = self.head
        count = 0
        while curnode != None:
            curnode = curnode.getNext()
            count = count + 1
        return count    
    
    def add(self,data):
        x = Node(data)
        x.setNext(self.head)
        self.head = x
        
    def append(self,data):
        x = Node(data)
        if self.head == None:
            self.head = x
            return
        curnode = self.head
        while curnode.nextnode:
            curnode = curnode.nextnode
        curnode.nextnode = x    
        
    
    def remove(self,data):
        curnode = self.head
        prevnode = None
        reqnode = False
        while not reqnode:
            if curnode.getValue() == data:
                reqnode = True
            else:
                prevnode = curnode
                curnode = curnode.getNext()
        if prevnode == None:
            self.head = curnode.getNext()
        else:
            prevnode.setNext(curnode.getNext())
            
    def search(self,data):
        curnode = self.head
        reqnode = False
        while curnode != None and not reqnode:
            if curnode.getValue() == data:
                reqnode = True
            else:
                curnode = curnode.getNext()
        return reqnode
    
    def printlist(self):
        curnode = self.head
        while curnode != None:
            print(curnode.getValue(),end=' ')
            curnode = curnode.getNext()
        print('') 

if __name__ == '__main__':
    l = LinkedList()
    
    print(l.isEmpty())
    
    l.add(1)
    l.add('linkedlist')
    l.printlist()
    l.append('lastvalue')
    l.printlist()
    print(l.search(1))
    l.remove(1)
    l.printlist()
