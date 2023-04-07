# In this example, the following if...else statement assigns 20 to the ticket_price if the age is greater than or equal to 18. Otherwise, it assigns the ticket_price 5:
age = input('Enter your age:')

if int(age) >= 18:
    ticket_price = 20
else:
    ticket_price = 5

print(f"The ticket price is {ticket_price}")

#To make it more concise, you can use an alternative syntax like this:
ticket_price = 20 if int(age) >= 18 else 5

#other languages does this:
#condition ? value_if_true : value_if_false with a question mark ?
