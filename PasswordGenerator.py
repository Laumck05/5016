import random
import string

def generate_random_password ():
    # Define charactors  for password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Password length
    password_length = 8
    #Generate random password
    password = "".join(random.choice(characters) for _ in range(password_length))
    return password 

