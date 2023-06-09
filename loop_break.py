# In this syntax, if the condition evaluates to True, the break statement terminates the loop immediately. It won’t execute the remaining iterations

for index in range(0, 10):
    print(index)
    if index == 7:
        break

for x in range(5):
    for y in range(5):
        # terminate the innermost loop
        if y > 1:
            break
        # show coordinates on the screen
        print(f"({x},{y})")