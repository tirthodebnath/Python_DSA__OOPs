#Largest element in the list
def max_num_in_list( list ):
    max = list[ 0 ]
    max1 = list[ 1 ]
    for i in list:
        if i > max:
            max = i
            # for j in range(1,len(list)):
            #     if j> max1:
            #         max1=j
    return max
print(max_num_in_list([1, 2, -8, 0]))


#######################################
##Not right Check again the code
# a=[30,40,3,5,6,100,2]
# target=a[0]

# for i in range(0,len(a)-1):
#     if target < a[i]:
#         target=a[i]
#     temp=a[0]
#     a[0]=a[i]
#     a[i]=temp
# print(a)
# target1=a[1]
# print("Largest Element:",target)
# print("2nd Largest Element:",target1)





    
        