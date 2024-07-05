shopping = []
while True:
    user = input("add to list \n")
    shopping.append(user) 
    if user == "":
        print("Your list was:")
# getting the range to tell how long to print list with range being the length of the list
        for i in range(len(shopping)):
            print(shopping[i])
        break