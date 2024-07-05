import colorama 
users = ["username", "1234"]
attempts = 0
while True:
    user = input(colorama.Fore.RESET +"whats your username? \n")
    passw = input("whats your passowrd? \n")
    if user == (users[0]) and passw == (users[1]):
        print(colorama.Fore.GREEN +"you got in")
        break
    else:
        print(colorama.Fore.RED + "try again")
        attempts = attempts + 1
    if attempts == 3:
        print("you are out of attempts!")
        break