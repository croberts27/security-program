# list of known users
known_users = ["Calvin", "McCall", "Boga", "Runey"]

while True:
    print("Hi, my name is Security Operating Ultra Program, but you can call me S.O.U.P. ")

    name = input("What is your name?: ").strip().capitalize()
    if name in known_users:
        print("Success! Hello, {}.".format(name))
        remove = input("Would you like to be removed from the system (y/n)?: ").lower()
        if remove == "y":
            print(known_users)
            known_users.remove(name)
            print(known_users)

        elif remove == "n":
            print("Great! Have a great day!")
    else:
        print("Error! Name not recognized.")