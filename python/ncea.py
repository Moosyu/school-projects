print("ncea check!!")
print("how many credits?")
credits = float(input())
print("how many literacy credits?")
litcreds = float(input())
print("how many numeracy credits?")
dankcreds = float(input())
total = dankcreds + litcreds + credits
if credits >= 80 and litcreds >= 10 and dankcreds >= 10:
    print("you passed!!")
else:
    print("you failed! you need", (100 - total), "more points to pass")