message1 = 'This is a string in Python'
message2 = "This is also a string"
message3 = '"Beautiful is better than ugly.". Said Tim Peters'
message4 = 'It\'s also a valid string' #To escape the quotes, you use the backslash (\)

#If you don’t want it to do so, you can use raw strings by adding the letter r before the first quote
message5 = r'C:\python\bin'

#Creating multiline strings
help_message = '''
Usage: mysql command
    -h hostname     
    -d database name
    -u username
    -p password 
'''
print(help_message,message1,message2,message3,message4,message5)