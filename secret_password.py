secret_password = "python123"
guess = ""
while guess != secret_password:
    guess = input("Enter password:")

if guess == secret_password:
    print("access granted")
else:
    print("wrong password")
