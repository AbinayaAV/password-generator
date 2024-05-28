import secrets
import string
import time

def generate_unique_secure_password(length=16):
   
    alphabet = string.ascii_letters + string.digits + string.punctuation
    random_part = ''.join(secrets.choice(alphabet) for i in range(length - 6))  
    timestamp = int(time.time() * 1000)
    unique_part = str(timestamp)[-6:]
    password = random_part + unique_part
    
    return password

unique_secure_password = generate_unique_secure_password(16)
print("Generated unique secure password:", unique_secure_password)
