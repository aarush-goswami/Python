class My_Books_Lab:
    def __init__(self):
        user = input("Enter user id : ")
        pin = input("Enter pin : ")
        if user == "user1" and pin == "1234":
            print("Login sucess\n")
            print("1.Art of war\n2.Atomic habits\n3.Broken\n")
        else:
            raise ValueError("Id or Password is wrong\n")


x = My_Books_Lab()
