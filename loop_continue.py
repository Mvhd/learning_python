#even numbers from 0 to 9:
for index in range(10):
    if index % 2:
        continue

    print(index)

# print the odd numbers 
counter = 0
while counter < 10:
    counter += 1

    if not counter % 2:
        continue

    print(counter)