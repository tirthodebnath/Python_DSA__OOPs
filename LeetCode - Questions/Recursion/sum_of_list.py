#sum of list with recursion 
#https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion-exercise-1.php

def list_sum(num_List):
    if len(num_List) == 1:
        return num_List[0]
    else:
        return num_List[0] + list_sum(num_List[1:])
        
print(list_sum([2, 4, 5, 6, 7]))
