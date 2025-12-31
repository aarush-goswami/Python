"""Functions in python
    Types of functions :
1.Predefine Function:-
Require Calling
function  definition Already present in library.


Modules:-In Python , module are files containing functions , variables  and other instructions .
In python ,We have !. Buuilfd In modules
 setup and stored in our system,no need to separetely installed )
 Build In modules (implement in C, implemented in python ,
 Standary Libarary Modules ,Third part modules  installed using PIP)





"""


# creating user define module
def show_user(list):
    print(list)
    print("\n")

def search_student(list):
    name = input("Enter Name of student to search : ")
    if name in list:
        print("Found\n")
    else:
        print("Not Found \n")


def add_student(list):
    name = input("Enter Name of student to add : ")
    if name not in list:
        list.append(name)
    print("Added successfully\n")


def delete_student(list):
    name = input("Enter name of student to delete : ")
    if name in list:
        list.remove(name)
        print("Delete successful\n")


"""
Micro architecture
solid principles
Tight/Loose coupling

Module 1 Search student
2 Add student
3 Delete student
4 start with new index.py file
5 welcome message + menu + login ?

"""
