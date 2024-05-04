from password import create_password, hash_it

print('Create a random password')
password = create_password()

hashed_password = hash_it(password)
print("Hashing your password using SHA-256 algorithm..." + '\n' + hashed_password)

def writing_password(): 
    filename = 'mypasswords.txt'
    with open(filename, 'a') as file:
        file.write(hashed_password + "\n")

writing_password()