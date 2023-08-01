#Initialise the heapq   
import heapq
heap = []
heapq.heappush(heap,10)
print(heap)

#Push to the heap
heapq.heappush(heap,20)
print(heap)

#Pop from the heap
heapq.heappop(heap)
print(heap)

#Heapify
import heapq
list1=[1,5,4,6,2,8,7]
heapq.heapify(list1)
print(list1)

#Heap-push-pop
heapq.heappushpop(list1,89)
print(list1)

#Heap-nsmallest Number
list2=[1,5,4,6,2,8,7,9]
print(heapq.nsmallest(1,list2))
print(heapq.nlargest(1,list2))

#priority queue
list3=[(1,"Ria"),(2,"Mia"),(3,"Sia"),(4,"Dia")]
heapq.heapify(list3)
print(list3)
for i in range(len(list3)):
    print(heapq.heappop(list3))