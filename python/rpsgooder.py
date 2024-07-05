import random
import time
rock = ["scissors", "lizard"]
paper = ["rock", "spock"]
scissors = ["paper", "lizard"]
lizard = ["spock", "paper"]
spock = ["scissors", "rock"]
# a shame that these need to be in same order to make it work but its fine probably also .lower isnt working maybe im dumb but things are case sensitive now :( 
rps = ["rock", "paper", "scissors", "lizard", "spock"]
megaList = [rock, paper, scissors, lizard, spock]
points = 0
while True:
    cpu = random.randint(0, 4)
    cpuMega = megaList[cpu]
    cpuRps = rps[cpu]
    player = (input("[1] Rock \n[2] Paper \n[3] Scissors \n[4] Lizard \n[5] Spock\n"))
    print("The computer played", cpuRps)
    if str(cpuMega) == str(megaList[int(player) - 1]):
        print("You tie!") 
    elif str(rps[int(player) - 1]) in str(cpuMega):
        print("You lose!")
        points -= 1
    else:
        print("You win!")
        points += 1
    print("You have", points, "points")
    time.sleep(1)
    escp = input("Write x to escape or nothing to continue \n")
    if escp == "x":
        break