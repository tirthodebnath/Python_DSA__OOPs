#stack is using list
stack=[]
def push():
    if len(stack)==n:
        print("List is full")
    element= input("Enter the element:")
    stack.append(element)
    print(stack)

def pop_element():
    if not stack:
        print("Stack is empty")
    else:
        e=stack.pop()
        print("Remove element:",e)
        print(stack)

n=int(input("Limit of stack:"))

while True:
    print("Select the element, 1:Push, 2:Pop, 3:Quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop_element()  
    elif choice==3:
        break
    else:
        print("Enter the correct operation")      