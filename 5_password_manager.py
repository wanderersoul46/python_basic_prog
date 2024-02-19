from cryptography.fernet import Fernet

# Function to load the encryption key from the key file
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

# Initialize Fernet with the loaded key
key = load_key()
fer = Fernet(key)

# Function to view stored passwords
def view():
    with open('password.txt', "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, encrypted_pass = data.split("/")
            # Decrypt and print the password
            print("User:", user, "Password:", fer.decrypt(encrypted_pass.encode()).decode())

# Function to add a new password
def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open('password.txt', "a") as f:
        # Encrypt and write the account name and password to the file
        f.write(name + "/" + str(fer.encrypt(pwd.encode()).decode()) + "\n")

# Main loop for user interaction
while True:
    mode = input("Would you like to add a new password or view existing ones? (view, add, q to quit): ")

    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode. Please enter 'view', 'add', or 'q' to quit.")
        continue
