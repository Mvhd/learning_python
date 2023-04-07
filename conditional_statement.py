# if condition:
#     if-block
# else:
#     else-block

age = input('Enter your age:')
if int(age) >= 18:
    print("You're eligible to vote.")

your_age = int(age)

# determine the ticket price
if your_age < 5:
    ticket_price = 5
elif your_age < 16:
    ticket_price = 10
else:
    ticket_price = 18

# show the ticket price
print(f"You'll pay ${ticket_price} for the ticket")