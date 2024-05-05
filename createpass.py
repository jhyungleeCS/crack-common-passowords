import hashlib
def new_password(): 
    passwrd1 = input("Enter a password to hash: ")
    print("Your password: ",passwrd1)
    return passwrd1


def hash_it(password): 
    hash_object = hashlib.sha256()
    hash_object.update(password.encode('utf-8'))
    return hash_object.hexdigest()


def writing_password(): 
    filename = 'myeasypasswords.txt'
    with open(filename, 'a') as file:
        file.write(hashed_password + "\n")

active = True 
while active: 
    password = new_password()
    hashed_password = hash_it(password)
    print("Hashed using SHA-256: ", hashed_password)
    writing_password()
    repeat = input("Hash another password?(y/n): ")
    if repeat == 'n':
        break 