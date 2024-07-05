from colorama import Fore

print(Fore.MAGENTA + "What is your weight in kgs?")
weight = input()
print(Fore.RED + "What is your height in metres")
height = input()
bmi =  float(weight) / float(height) * float(height)
print("Your bmi is", bmi)
if bmi < 18.5:
   print(Fore.BLUE +"You are underweight")
elif bmi > 25:
    print(Fore.LIGHTRED_EX +"You are overweight")
else:
    print(Fore.LIGHTGREEN_EX + "You weight good")
