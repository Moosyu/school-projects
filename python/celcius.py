forever = True
print("write x to escape")
while forever == True:
    print("Please enter a temprature in Fahrenheit")
    f = input()
    if f == "x":
        break
    else:
        c = (float(f) - 32) * 5 / 9
        print("Your temprature in Celcius is ", c) 
