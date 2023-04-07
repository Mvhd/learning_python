# Introduction to Python comments

# 1. Python block comments
# increase price by 5%
price1 = 100
price = price1 * 1.05

# 2. Python inline comments
salary1 = 100
salary = salary1 * 1.02   # increase salary by 2%

# 3. Python docstrings
# Unlike a regular comment, a documentation string can be accessed at run-time using  obj.__doc__ attribute where obj is the name of the function.

def increase(salary, percentage, rating):
    """ increase salary base on rating and percentage
    rating 1 - 2 no increase
    rating 3 - 4 increase 5%
    rating 4 - 6 increase 10%
    """