import os
from cryptography.fernet import Fernet

files = []

# Provide the encryption key here
key ="" 
with open('key','rb') as secKey:
    key=secKey
crypt = Fernet(key)

# Function to decrypt a file
def decrypt_file(file_path):
    with open(file_path, 'rb') as encrypted_file:
        encrypted_content = encrypted_file.read()
        decrypted_content = crypt.decrypt(encrypted_content)
    return decrypted_content

# Iterate through each file in the directory
for file in os.listdir():
    # Exclude the script file and only process encrypted files
    if file != "encrypt.py" and file.endswith(".encrypted"):
        files.append(file)

# Decrypt each file
for encrypted_file in files:
    decrypted_content = decrypt_file(encrypted_file)
    
    # Get the original file name without the ".encrypted" extension
    original_file_name = encrypted_file[:-10]
    
    # Write the decrypted content to a new file
    decrypted_file_path = "decrypted_" + original_file_name
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_content)

print("Files Decrypted")
