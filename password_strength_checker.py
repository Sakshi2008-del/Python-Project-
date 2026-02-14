password = input("enter your password :")

has_digit = False
has_special = False
has_upper = False
has_lower = False

if len(password) >= 0 :
    for char in password :
        if char.isdigit():
            has_digit = True
        elif char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isalnum :
            has_special = True

    if has_special and has_digit and has_lower and has_upper :
        print("strong password")
    else :
        print("weak password")

else :
    print("your password is too short ")
