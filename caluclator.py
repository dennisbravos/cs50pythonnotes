def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

#raise to the power of 2 use (**) or power use pow(n, 2)

def square(n):  
    return n * n


main()


x = float(input("What's x? "))
y = float(input("What's y? "))

#z = round(x + y)

z = round(x / y, 2)

#numbers with commas (,)
print(f"{z:,}")