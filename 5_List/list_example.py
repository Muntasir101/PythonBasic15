student_details = []

"""
student_name = input("name: ")
student_email = input("email: ")
student_age = float(input("age: "))

student_details.append(student_name)
student_details.append(student_email)
student_details.append(student_age)

print(student_details)
"""

# number_elements = int(input("number_elements: "))

"""
for _ in range(1):
    student_name = input("name: ")
    student_email = input("email: ")
    student_age = float(input("age: "))

    user_info = {
        "name": student_name,
        "email": student_email,
        "age": student_age
    }
    student_details.append(user_info)

print(student_details)
"""

"""
even_number = []
odd_number = []

max_number = int(input("Enter max number: "))

for number in range(1, max_number + 1):
    if number % 2 == 0:
        even_number.append(number)
    else:
        odd_number.append(number)

print(even_number)
print(odd_number)
"""

number_list = [12, 33, 45, 6, 8, 90, 3]

even_number = []
odd_number = []

for number in number_list:
    if number % 2 == 0:
        even_number.append(number)
        sorting = even_number.sort(reverse=False)
    else:
        odd_number.append(number)
        sorting = odd_number.sort(reverse=False)

print(even_number)
print(odd_number)