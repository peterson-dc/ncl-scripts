def crack(user_input, num):
    password = ''
    for char in user_input:
        if char == ' ':
            password += ' '
        else:
            order = ord(char) - num
            if order < 97:
                order = 123 - (97 - order)
            password += chr(order)
    print(password)



user_input = input("Enter the string: ")
for i in range(1, 27):
    crack(user_input, i)
