import sys

db = {}


def print_db():
    if len(db) == 0:
        print("Empty\n")
        return 1
    for key, value in db.items():
        print(f"Name : {key}")
        for k, v in value.items():
            print(f"{k} : {v}")
        print("\n")


def create_record():
    try:
        x = {}
        name = input("Enter name : ").title()
        x["r_no"] = input("Enter roll no. : ")
        x["Branch"] = input("Enter Branch : ")
        x["Year"] = input("Enter year : ")

        db[name] = x
        print("Added Sucessfully... \n")
    except:
        raise ValueError("Some wrong input entered\n")


def del_record(name):
    if name in db.keys():
        del db[name]
    else:
        print("Student Not Found ...\n")


if __name__ == "__main__":
    while True:
        ch = int(
            input(
                f"1.Add student record\t2.Delete Student record\n3.Print all students\t4.Exit  "
            )
        )
        match ch:
            case 1:
                create_record()
            case 2:
                name = input("Enter name : ").title()
                del_record(name)
            case 3:
                print_db()
            case 4:
                print("Thankyou :)\n")
                sys.exit(0)
