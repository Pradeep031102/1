# Password Vaildation

def validate_password(password):
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
    elif not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter.")
    elif not any(char.isdigit() for char in password):
        print("Password must contain at least one digit.")
    else:
        print("Password is valid.")

password = input("Create your password: ")
validate_password(password)
