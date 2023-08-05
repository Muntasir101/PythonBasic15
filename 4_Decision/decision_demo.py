pass_marks = 40
while True:
    try:
        marks = float(input("Enter marks: "))
        break
    except ValueError:
        print("Invalid Input. Please enter number")

if marks >= pass_marks:

    if 40 <= marks < 50:
        print("Grade D")

    elif 50 <= marks < 60:
        print("Grade C")

    elif 60 <= marks < 70:
        print("Grade B")

    elif 70 <= marks < 80:
        print("Grade A")

    elif 80 <= marks <= 100:
        print("Grade A+")

    else:
        print("invalid Marks")

else:
    print("Failed")



