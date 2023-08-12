user_details = {
    'first_name': 'John',
    'last_name': 'smith',
    'email': 'john.smith@gmail.com',
    'phone': 123456,
    'marks': [20, 30, 50],
    'address': {
        'permanent_address': {
            'district': "Dhaka",
            'road': "A002"
        },
        'present_address': {
            'district': "Sylhet",
            'road': "S101"
        }
    }
}

# Length of the dictionary
length = len(user_details)
print(length)

# Extract item from the dictionary
print(user_details['first_name'])

# Get all keys from the dictionary
all_keys = user_details.keys()
print(all_keys)

# Get all keys from the dictionary as list
key_list = list(user_details)
print(key_list)


# Get all values from the dictionary
all_values = user_details.values()
print(all_values)

# Get all values from the dictionary as list
all_values_list = list(user_details.values())
print(all_values_list)

# Add a new key to the dictionary
user_details['password'] = "123456"

# Add a new item to the list
user_details['marks'].append(60)

print(user_details)

# get data from nested dictionary
print(user_details['address']['permanent_address']['road'])

print(list(user_details.items()))

print(user_details['marks'])
