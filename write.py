from main import hashed_password
def writing_password(): 
    filename = 'mypasswords.txt'
    with open(filename, 'a') as file:
        file.write(hashed_password)