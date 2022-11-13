import random
import string
from random import sample

def get_random_password(n=8):
    chars = string.ascii_uppercase + string.ascii_lowercase +string.digits
    password_chars_list = random.sample(chars, n)
    password = ""
    for i in range(n):
        password += str(password_chars_list[i])
    return password

print(get_random_password())
