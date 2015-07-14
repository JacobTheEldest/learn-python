#This program requires a username and password that the user can set
user = input("Create user: ")
password = input("Create password: ")
action = ""

while action != "quit":
    if action == "help":
        print("Available actions:")
        print("help")
        print("lock")
        print("change_user")
        print("change_pass")
        print("whoami")
        print("quit")

    if action == "lock":
        user_ans = " "
        pass_ans = " "
        while user_ans != user:
            user_ans = input("Username: ")
            
            if user_ans != user:
                print("User:", user_ans, "does not exist.")

        while pass_ans != password:
            pass_ans = input("Password: ")

            if pass_ans != password:
                print("Password incorrect.")
        print("Unlocked!")

    if action == "change_user":
        pass_ans = input("Password: ")

        if pass_ans == password:
            user = input("New user: ")
        else:
            print("Password incorrect.")

    if action == "change_pass":
        pass_ans = input("Old password: ")

        if pass_ans == password:
            password = input("New password: ")
        else:
            print("Password incorrect.")

    if action == "whoami":
        print(user)

    action = input("> ")
