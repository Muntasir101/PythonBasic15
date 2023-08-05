"""
children( age 0 to 12) get 50% discount
teenagers( age 13 to 17) get 25% discount
adults(18 to 64) pay full price
seniors(above 64) get 100% discount
"""

purchase_amount = 100

age = int(input('enter your age: '))

if 0 <= age <= 12:
    final_price = purchase_amount * 0.5

elif 13 <= age <= 17:
    discount = purchase_amount * 0.75

elif 18 <= age <= 64:
    final_price = purchase_amount

elif age >= 65:
    final_price = purchase_amount - purchase_amount

print("You have to pay: ", final_price)