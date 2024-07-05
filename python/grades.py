while True:
    name = input("whats your name? \n")
    score = float(input("whats your score \n"))
    maxScore = float(input("what was the tests max score? \n"))
    percentage = score / maxScore * 100
    if percentage >= 80:
        print(name, "you got", round(score), "/", round(maxScore), "you got an a! 😎")
    elif percentage < 80 and percentage >= 65:
        print(name, "you got", round(score), "/", round(maxScore), "you got an b! 🤓")
    elif percentage < 65 and percentage >= 50:
        print(name, "you got", round(score), "/", round(maxScore), "you got an c! 😐")
    elif percentage < 64 and percentage >= 40:
        print(name, "you got", round(score), "/", round(maxScore), "you got an d! 😭")
    else:
        print(name, "you got", round(score), "/", round(maxScore) , "you got an f! 💀")
    quit = input("type x to quit, type anything to stay \n").lower()
    if quit == "x":
        break