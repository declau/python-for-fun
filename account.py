
bank_amount = 100
item_one = 25
item_two = 30
item_three = 15
final_amount = bank_amount - item_one - item_two - item_three
print(final_amount)

items = [item_one, item_two, item_three]

# For
for item in items:
    bank_amount = bank_amount - item
print(bank_amount)
