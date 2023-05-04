##Python Program to find Smallest number among three.

a =[10,5,3]
b=0


def smallest_3():
    for i in a:
        if a[0]>a[1] and a[0]>a[2] :
            print(a[0],"Biggest")
        elif a[1]>a[0] and a[1]>a[2]:
            print(a[1],"Biggest")
        else:
            print(a[2],"Biggest") 

smallest_3()
