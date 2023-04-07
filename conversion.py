#To get input from users, you use the input() function. For example:
value = input('Enter a value:')
print(value)
price = input('Enter the price ($):')
tax = input('Enter the tax rate (%):')

net_price = price * tax / 100

print(f'The net price is ${net_price}')
#… you’ll get the following error:

# Traceback (most recent call last):
#   File "app.py", line 4, in <module>
#     net_price = price * tax / 100
# TypeError: can't multiply sequence by non-int of type 'str'

# Since the input values are strings, you cannot apply the arithmetic operator (+) to them.
# To solve this issue, you need to convert the strings to numbers before performing calculations.
# To convert a string to a number, you use the int() function. More precisely, the int() function converts a string to an integer.
# The following example uses the int() function to convert the input strings to numbers:

price = input('Enter the price ($):')
tax = input('Enter the tax rate (%):')
net_price = int(price) * int(tax) / 100
print(f'The net price is ${net_price}')