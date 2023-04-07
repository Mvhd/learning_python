# Falsy and Truthy values
# When a value evaluates to True, it’s truthy. And if a value evaluates to False, it’s falsy.

# The following are falsy values in Python:

# The number zero (0)
# An empty string ''
# False
# None
# An empty list []
# An empty tuple ()
# An empty dictionary {}

is_active = True
is_admin = False

a = 20
b = 10
print(a > b) #true
print(a < b) #false

c = 'a'
d = 'b'
print(c < d) #true
print(c > d) #false

hi = bool('Hi') #True
emptybool = bool('') #False
number100 = bool(100) #True
numberzero = bool(0) #False
print(hi)
print(emptybool)
print(number100)
print(numberzero)