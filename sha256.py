import hashlib
import base64
from Crypto.Cipher import AES

encrypted = hashlib.sha256(b"...").hexdigest()
print(encrypted)

# save file
encryptedContent = str(encrypted)
with open('sha256.txt', 'w') as f:
    f.write(encryptedContent)
    f.close()
