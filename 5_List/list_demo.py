student_name = ['Student1', 'Student2', 'Student3', 'Student4', 'Student5']

# Length of the list
total_student = len(student_name)
print(total_student)

# Extract first item from the list
first_item = student_name[0]
print(first_item)

# Extract lst item from the list
last_item = student_name[total_student - 1]
print(last_item)

# Check if the item is in the list
if 'Student5' in student_name:
    print("True")
else:
    print("False")

# add new item to the list
student_name.append("Student6")

print(student_name)

# add new item to the list in specified position
student_name.insert(0, 'smith') # ['smith', 'Student1', 'Student2', 'Student3', 'Student4', 'Student5', 'Student6']
print(student_name)

# delete item
failed_student = student_name.pop(1)
print(student_name)
print(failed_student)

# remove item from the list
student_name.remove('Student3')
print(student_name)


student_name.clear()
print(student_name)