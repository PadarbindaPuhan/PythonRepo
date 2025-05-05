def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x,y):
    return x*y

def division(x,y):
    if y == 0:
        return "Can not divide by zero!"
    return x/y

def square(x):
    return x*x

def cube(x):
    return x*x*x

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Diision")

choice = input("Enter choice (1/2/3/4/5/6): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", subtract(num1, num2))
elif choice == '3':
    print("Result:", multiply(num1, num2))
elif choice == '4':
    print("Result:", division(num1, num2))
elif choice == "5":
    print("Result:", square(num1))
elif choice == '6':
    print("Result:", cube(num1))
else:
    print("Invalid input")
