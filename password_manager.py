# PASSWORD MANAGER
""""
storage all the passwords in a txt file cripting it
"""
from cryptography.fernet import Fernet 
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return  key



key = load_key() 
fer = Fernet(key)

# view de passwords 
def view():
    with open("password.txt",'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:", 
                fer.decrypt(passw.encode()).decode())

#add a new password
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    with open("password.txt",'a') as f:
        #encrypt the password before saving it using fer and encode encode to converte to bytes
        f.write(name+" | "+ fer.encrypt(pwd.encode()).decode() + "\n")

    
    
while True:
    mode = input("Whould you like to add a new password or view existing ones (view, add)? press q to quit ").lower()
    
    if mode =="q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode!")  
        continue

