import random 
import string 
import hashlib


characters = string.ascii_letters + string.digits

def create_password(): 
    password = ''
    while True:
        try: 
            count = int(input("How many characters do you want in your password?(Recommended 8 characters minimum): "))
        except ValueError:
            print("Must be a numerical value.")
        else:
            password = password.join(random.choice(characters) for _ in range(count))
            print("Your password is: " + "\n" + password)
            return password


def hash_it(password): 
    hash_object = hashlib.sha256()
    hash_object.update(password.encode('utf-8'))
    return hash_object.hexdigest()
    
