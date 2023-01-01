# sort the list with key 'id'

nodes = [
{
    "name" : "A",
    "id" : 27,
    "pid": 3
},
{
    "name" : "B",
    "id" : 3,
    "pid" : 1
},
{
    "name" : "C",
    "id" : 42,
    "pid" : 1
},
{
    "name" : "D",
    "id" : 11,
    "pid" : 2
},
{
    "name" : "E",
    "id" : 23,
    "pid" : 4   
}
]

l2={}
j= 1
for i in nodes:
    print(i)
    for key,value in i.items():
        if key == "id":
            l2[j]= value
            j = j+1
l2 .sort()          
print(l2) 
  