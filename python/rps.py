import random

rps = ["Rock", "Paper", "Scissors", "Lizard"]

cpu = rps[random.randint(0, 3)]

player = int(input("[1] Rock \n[2] Paper \n[3] Scissors \n[4] Lizard \n"))

print("computer picked", cpu)

if cpu == rps[player - 1]:
    print("you tie",)
elif cpu == rps[0] and player == 3 or cpu == rps[1] and player == 1 or cpu == rps[2] and player == 2 or player == 4 and rps[1] :
    print("cpu wins")
else:
    print("you win")