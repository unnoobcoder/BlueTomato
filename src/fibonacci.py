def fibonacci():
    x = 1
    while x < 2000:
        old = x - x
        x = x + old

        print(x)
fibonacci()