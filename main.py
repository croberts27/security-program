# list of known users
known_users = ["Calvin", "McCall", "Boga", "Runey"]

while True:
    print("HI!! My name is Security Onions Ultra Potatoes! You can call me S.O.U.P. ")

    name = input("What is your name?: ").strip().capitalize()
    if name in known_users:
        print("Success! Hello, {}.".format(name))
        remove = input("Would you like to be removed from the system (y/n)?: ").lower()
        if remove == "y":
            known_users.remove(name)

        elif remove == "n":
            print("WONDERFUL NEWS!!! Have a great day!")
            break
    else:
        print("Hmm. I don't think I've met you yet, {}.".format(name))
        add_user = input("Would you like to be added to the system? (y/n)?: ").lower()
        if add_user == "y":
            known_users.append(name)
            print("Hooray! THANK YOU FOR JOINING THE S.O.U.P. SYSTEM!")
            print("Have a nice day!")
            break
        elif add_user == "n":
            print("WHAT?? PLEASE RECONSIDER!!")