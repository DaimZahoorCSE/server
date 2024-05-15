import os
from cryptography.fernet import Fernet

files = []

key = Fernet.generate_key()
crypt = Fernet(key)

# Exclude the script file from the list of files
for file in os.listdir():
    if file != "encrypt.py":
        files.append(file)

# Encrypt each file
for file in files:
    with open(file, 'rb') as fileToEncrypt:
        content = fileToEncrypt.read()
        encryptedFileData = crypt.encrypt(content)
    
    # Write the encrypted content to a new file
    encrypted_file_path = file + ".encrypted"
    with open(encrypted_file_path, 'wb') as encryptedFile:
        encryptedFile.write(encryptedFileData)

print("Files Encrypted")
print("Encryption Key:", key.decode())  # Convert bytes to string for printing
