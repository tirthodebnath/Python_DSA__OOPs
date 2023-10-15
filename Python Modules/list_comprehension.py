##List comprehension

lst= [1,2,3,4,5,6,7]

even=[i for i in lst if i%2==0]
print("Even:",even)

odd=[i for i in lst if i%2!=0]
print("Odd:",odd) 