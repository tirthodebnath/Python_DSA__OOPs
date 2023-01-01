##How to find a missign value from a list of integers

mylist=[1,2,3,4,5,7,8,9,10]

def find_lst(n):
    sum1= n*(n+1)/2
    sum2= sum(mylist)

    print(sum1 - sum2)

find_lst(10)