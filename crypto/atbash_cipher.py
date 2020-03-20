def crack(user_input):
    password = ''
    for char in user_input:
        if char == ' ':
            password += ' '
        else:
            diff = ord(char) - 97
            order = ord(char) + (25 - (2 * diff))
            password += chr(order)
    print(password)



user_input = input("Enter the string: ")
crack(user_input)
