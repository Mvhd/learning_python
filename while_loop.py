# while condition:  
#    body

max = 5
counter = 0

while counter < max:
    print(counter)
    counter += 1

#  Using the Python while statement to build a simple command prompt program
command = ''

while command.lower() != 'quit':
    command = input('>')
    print(f"Echo: {command}")
