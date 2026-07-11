ddd = input("enter your new password is your password")
print("your password has been added")
fff = input("what is your password")
while fff != ddd:
    print("Incorrect! Try again.")
    fff = input("what is your password: ").strip()
print("Correct!\n")
