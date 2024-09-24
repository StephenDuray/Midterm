num_stacks = int(input("Enter how many stacks you want to enter: "))
container = []

for i in range(1, num_stacks + 1):
    stack = input(f"Enter Stack {i}: ")  
    container.append(stack) 


if len(container) > 1:
    result = ", ".join(container[:-1])+ ", " + " and " + container[-1] 
else:
    result = container[0] 

print(f"You have stacks of: {result}")


def ask_remove():
    try:
        remove = input("Click R to Remove: ")
        if remove == "R":
            if container:
                container.pop()
                if container:
                    if len(container) > 1:
                     print("The stacks remaining are: " + ", ".join(container[:-1])+ ", " + "and " + container[-1] )
                    else:
                        print("The stacks remaining are: " + container[0])
                else:
                 print("All stacks have been removed.")

            else:
                print("You do not have a stack left.")
                
        return ask_remove()
    except:
        return ask_remove()
        
ask_remove() 