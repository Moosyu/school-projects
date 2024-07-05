x = 0
y = 1
count = 0
print("how many sequences you want?")
sequences = float(input())
while count <= sequences:
       print(x)
       z = x + y
       x = y
       y = z
       count += 1
# whoops did the wrong thing turned out fine though