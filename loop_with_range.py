# for index in range(n):
#     statement
# range(start, stop)
for index in range(5):
    print(index)

for index1 in range(1, 6):
    print(index1)

# range(start, stop, step)

for index2 in range(0, 11, 2):
    print(index2)

# Using Python for loop to calculate the sum of a sequence

sum = 0
for num in range(101):
    sum += num
    print(sum)

# How it works.

# First, the sum is initialized to zero.
# Second, the sum is added with the number from 1 to 100 in each iteration.
# Finally, show the sum to the screen