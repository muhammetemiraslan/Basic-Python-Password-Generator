import random
import string

def generate_secure_password(length=12): # PASSWORD LENGTH
    characters = string.ascii_letters + string.digits + string.punctuation
    secure_password = ''.join(random.choice(characters) for _ in range(length))
    return secure_password

if __name__ == "__main__":
    password_length = 16  # passwd lenght.
    secure_password = generate_secure_password(password_length)
    print("password generated:", secure_password)

    file_name = input("file Name (password.txt): ")

    with open(file_name, 'w') as file:
        file.write(secure_password)

    print("Saved Success:", file_name)
