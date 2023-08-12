# function without arguments
def summation():
    number1 = 10
    number2 = 20
    print(number1 + number2)


summation()


# function with arguments
def subtract(number1=50, number2=30):
    print(number1 - number2)


subtract(100, 500)


def multiply(number1, number2):
    return number1 * number2


def multiply2(number1, number2):
    return number1 * number2


print(multiply(10, 20))


def calculator():
    return multiply(10, 50) + multiply2(50, 10)


print(calculator())


def subtract2():
    number1 = int(input("Number 1: "))
    number2 = int(input("Number 2: "))
    return number1 - number2


print(subtract2())
