height = []
add = float(input("how many people?\n"))
newHeight = 0
while True:
    high = float((input("enter heights \n")))
    height.append(high)
    newHeight = newHeight + high
    if len(height) == add:
        print("lowest is", min(height))
        print("highest is", max(height))
        print("average is", newHeight / add)
        break