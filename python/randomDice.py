import random
print("enter the number of sides you want 1: d4, 2: d6, 3: d8, 4: d10, 5: d12, 6: d20 or write x to escape")
while True:
    f = input()
    if f == "x":
        break
    x = (4 + 2 * int(f) - 2)
    if x >= 14:
        x = 20
    print("you got", random.randint(1, x) + random.randint(1, x))