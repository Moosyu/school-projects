print("age?")
age = int(input())

if age > 130 or age < 0:
    print("incorrect")
    print("age?")
    age = int(input())
elif age > 59 and age < 68:
    print("boomer")
elif age > 42 and age < 59:
    print("gen x")
elif age > 26 and age < 43:
    print("millennial")
elif age > 10 and age < 27:
    print("gen z")
elif age > 0 and age < 10:
    print("gen alpha")
