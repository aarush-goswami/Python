db = []


def add_student():
    try:
        name, id, sem = input("Enter data name  id  sem : ").split()
        data = (name, int(id), sem)
        db.append(data)
        print("Data added sucessfully \n")
    except ValueError as ve:
        print(ve)


def delete_student(id):
    for i in range(len(db)):
        if db[i][1] == id:
            del db[i]
            return 1
    print("Not found\n")


def view_db():
    if db:
        for data in db:
            print(f"Name : {data[0]}\tId : {data[1]}\tSem : {data[2]}\nDeleted Sucessfully\n")
    else:
        print("Empty\n")


if __name__ == "__main__":
    while True:
        ch = int(
            input("1.Add student\n2.Delete Student\n3.View all students\n4.Exit\t ")
        )
        match ch:
            case 1:
                add_student()
            case 2:
                id = int(input("Enter id : "))
                delete_student(id)
            case 3:
                view_db()
            case 4:
                print("Goodbye :) \n")
                break
