import sys

user_admin = "admin"
pass_admin = "admin1234"

user_prompt = input("Username: ")
pass_prompt = input("Password: ")

if user_prompt == user_admin and pass_prompt == pass_admin:
    print("Logat!")
else:
    print("User sau parola gresita!")
    sys.exit(404)

print("Mesaj dupa logare....")