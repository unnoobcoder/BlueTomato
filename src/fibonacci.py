# def fibonacci():
#    x = 1
#    while x < 2000:
#        old = x - x
#        x = x + old        # Old fibonnaci code
#
#        print(x)
# fibonacci()


fib=[0,1]
for i in range(50):
    fib.append(fib[-1]+fib[-2])         #easier and smarter code
print(fib)