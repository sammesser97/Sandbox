MINIMUM_LENGTH = 4

password = input("Enter password of at least {} characters: ".format(MINIMUM_LENGTH))
while len(password) < MINIMUM_LENGTH:
    password = input("Enter password of at least {} characters: ".format(MINIMUM_LENGTH))
print('*' * len(password))
