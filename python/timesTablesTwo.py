x = 1
y = 1
z = 1
while x <= 12:
    print(y, "x", x, "=", y * x)
    x += 1
    if x == 13:
        y += 1
        x = 1
        z += 1
    if z == 13:
        break