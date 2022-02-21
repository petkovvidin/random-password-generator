import string
import random

length = int(input('Enter password length: '))
special = str(input("Do you want special chars? y/n : "))
if special == 'y':
    special_chars = '!@#$%^&*()'
else:
    special_chars = ''

chars = list(string.ascii_letters + string.digits + special_chars)
password = []

for i in range(length):
    random.shuffle(chars)
    password.append(random.choice(chars))

print('Your password is: ' + ''.join(password))
