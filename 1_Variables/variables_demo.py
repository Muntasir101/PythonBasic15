"""
Numeric Type:
integer: int
float: float
string: string

"""

age = 20
print(age)

tax = 10.5
print(type(tax))

address1 = 'dhaka'
My_name = "smith"

# case sensitive
number1 = 10

my_details = 'smith 22'

name = 'John Smith'
address = 'Dhaka'
email = 'john.smith@gmail.com'
phone = '555-333-22'

print(name, address, email, phone)
# escape sequences
print(name + '\n' + address + '\n' + email + '\n' + phone)

# assign multiple values
student1, student2, student3 = 'John Smith1', 'John Smith2', 'John Smith3'

# one value to multiple variables
student4 = student5 = student6 = "John SmithN"
print(student6)

# type conversion
number5 = float(number1)
print(type(number1))
print(type(number5))

number6 = int(number5)
print(type(number6))

name = str(22)
print(name)
print(type(name))