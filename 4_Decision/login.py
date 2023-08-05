default_username = 'admin'
default_password = 1234

username = input("enter your username: ")
password = int(input("enter your password: "))

if username == default_username and password == default_password:
    print("Login successful")
else:
    print("Login failed")
