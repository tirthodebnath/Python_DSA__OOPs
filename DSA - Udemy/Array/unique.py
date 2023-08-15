# l=[1,4,3,2,4]
# l2=[]

# def uniq(l):
#     for i in l:
#         if i in l2:
#             print(i)
#             return False
#         else:
#             l2.append(i)
#     return True

# print(uniq(l))

#################################################################

def printUnordered(arryA,arrayB):
    for i in range(len(arryA)):
        for j in range(len(arrayB)):
            if arryA[i] < arrayB[j]:
                print(str(arryA[i]) + ","+ str(arrayB[j]))

arrayB =[ 1,2,3,4,5,6]
arryA = [1,2,3,4,5,6,7,8,9,10]

printUnordered(arrayB,arryA)   