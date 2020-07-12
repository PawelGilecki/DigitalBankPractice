import string
import random

low_chars = list(string.ascii_lowercase)
upper_chars = list(string.ascii_uppercase)
digits = list(string.digits)
special_chars = list(string.punctuation)
all_chars = low_chars+upper_chars+digits+special_chars

def generatePassword():
    password = random.choice(low_chars)
    password += random.choice(upper_chars)
    password += random.choice(digits)
    password += random.choice(special_chars)

    for i in range(4):
        password += random.choice(all_chars)
    password_list = list(password)
    random.shuffle(password_list)
    password =''.join(password_list)

    return password
