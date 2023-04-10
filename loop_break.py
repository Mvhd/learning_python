# In this syntax, if the condition evaluates to True, the break statement terminates the loop immediately. It won’t execute the remaining iterations

for index in range(0, 10):
    print(index)
    if index == 7:
        break