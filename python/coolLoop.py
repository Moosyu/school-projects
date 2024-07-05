import colorama
import random
x = 0
text= "I will not misbehave in class"

while x != 150:
    x += 1
    colors = list(vars(colorama.Fore).values())
    colored_word = [
        random.choice(colors) ]
    print(x, text, ''.join(colored_word))
