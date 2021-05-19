""" Max heap is implemented.
    For min heap, reverse the heapify function."""
def heapify(ar,size,i):
    largest = i
    lc = 2*i+1
    rc = 2*i+2

    if lc<size and ar[lc]>ar[i]:
        largest = lc
    if rc<size and ar[rc]>ar[largest]:
        largest = rc

    if largest != i :
        ar[i],ar[largest] = ar[largest],ar[i]
        heapify(ar,size,largest)

def insert(ar,value):
    size = len(ar)
    if size ==0:
        ar.append(value)
    else: 
        ar.append(value)    
        for i in range((size//2)-1,-1,-1):
            heapify(ar,size,i)

def removeNode(ar, value):
    size = len(ar)
    i = 0
    for i in range(size):
        if value == ar[i]:
            break
    ar[i],ar[size-1] = ar[size-1],ar[i]
    ar.remove(value)
    size = len(ar)

    for i in range((size//2)-1,-1,-1):
        heapify(ar,size,i)

ar =[]

insert(ar,5)
insert(ar,8)
insert(ar,3)
print(ar)

removeNode(ar,8)
print(ar)
