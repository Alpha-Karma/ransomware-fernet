import os
from cryptography.fernet import Fernet

files = []
for file in os.listdir():
    if file == "ransomware.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)
        
print(files)

with open("thekey.key", "rb") as key:
    secretkey = key.read()
    
passphrase = "1234"
upassword = input("Enter the password: ")
if upassword == passphrase:
    for file in files:
        with open(file, "rb") as thefile:
            content = thefile.read()
        content_decrypt = Fernet(secretkey).decrypt(content)
        with open(file, "wb") as thefile:
            thefile.write(content_decrypt)
        print("Yo recovered all your files!!")
else:
    print("SENHA ERRADA")
    
