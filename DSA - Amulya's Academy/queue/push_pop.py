#Push and pop in queue
'''
queue=[]
def enqueue():
    if len(queue)==n:
        print("List is full")
    element= input("Enter the element:")
    queue.append(element)
    print(queue)

def dequeu():
    if not queue:
        print("queue is empty")
    else:
        e=queue.pop()
        print("Remove element:",e)
        print(queue)

n=int(input("Limit of queue:"))

def display():
    print(queue)

while True:
    print("Select the element, 1:add, 2:remove, 3:show, 4:Quit")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        queue()  
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("Enter the correct operation") '''



#De-queue implementation...................
'''
import collections
q=collections.deque()
print(q) 

#append-left
q.appendleft(10)
q.appendleft(20)
q.appendleft(30)
q.appendleft(40)

print(q)

#pop-left
q.popleft()
print(q)

print(q[2]) '''

#priority queue...........

q=[]

q.append(10)
q.append(20)
q.append(30)
q.sort()
q.append(40)
q.sort()

print(q)

q.pop()

print(q)

q.pop()

print(q)


