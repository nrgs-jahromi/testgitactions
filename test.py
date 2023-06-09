def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def modulo(x, y):
    return x % y

def print_result(result):
    print("Final result:", result)

x = int(input("Enter the first number : "))
y = int(input("Enter the second number : "))


sum_result = add(x, y)
print("Sum:", sum_result)


difference = subtract(x, y)
print("Difference:", difference)


product = multiply(x, y)
print("Product:", product)


remainder = modulo(x, y)
print("Remainder:", remainder)

