stack=[]

def push():
    if len(stack)==n:
        print("List is full")
    else:    
        element = input("Enter the element:")
        stack.append(element)
        print(stack)

def pop():
    if not stack:
        print("Stack is empty.")
    else:
        e=stack.pop()
        print("Remove element",e)
        print(stack)

n=int(input("limit of the stack:"))

while True:
    print("Select any one of the operation, 1: Push, 2: Pop, 3: quit")

    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        break
    else:
        print("Enter the correct operation")        



