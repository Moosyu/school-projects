# not really a school project i just needed something done so im just gonna throw this into here. divides a value in a json file by 10.
import json
import math

fileName = input("what is your json file's name (don't include the file extension): ")
valueName = input("what is the name of the value you want to change in your json file (eg: score): ")

with open(fileName.strip() + ".json", "r") as load:
    data = json.load(load)

for n in data:
    score = n[valueName]
    
    if str(score).endswith("0"):
        n[valueName] = math.trunc(int(score) / 10)
    else:
        n[valueName] = int(score) / 10 

with open(fileName.strip() + ".json", "w") as save:
    json.dump(data, save, indent=6)

print("done!!")
