import random
answer = random.randint(1, 100)
print("ive picked a number between 1 and 100, guess it")
while True:
    inputs = int(input())
    if inputs < answer:
        print("the number is bigger than", inputs)
    elif inputs > answer:
        print("the number is smaller than", inputs)
    else:
        print("you got it correct")
        break