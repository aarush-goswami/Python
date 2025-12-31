deps = []
daily_wager = {}
regular = {}


class Department:
    def __init__(self, did, name):
        self.did = did
        self.name = name
        deps.append(name)


class Employee:
    def __init__(self, eid, name):
        self.eid = eid
        self.name = name


class DailyWager(Employee):
    def __init__(self, eid, name, wage, days):
        super().__init__(eid, name)
        self.salary = wage * days
        daily_wager[eid] = {"name": name, "salary": self.salary}


class Regular(Employee):
    def __init__(self, eid, name, basic, da, hra):
        super().__init__(eid, name)
        self.salary = basic + da + hra
        regular[eid] = {"name": name, "salary": {self.salary}}


def print_regular():
    for key, value in regular.items():
        print(f"{key} : {value}")
    print("\n")


def print_daily_wager():
    for key, value in daily_wager.items():
        print(f"{key} : {value}")
    print("\n")


def display_departments():
    for i in deps:
        print(i, end=" ")
    print("\n")


s = f"""
1.Insert Employee Details
2.Update Salary
3.Delete Employee Record
4.Search Employee
5.Display employee
6.Display departments
7.Exit
"""
while True :
    print("Employee database".center(30,"="))
    ch = int(input(s))
    match ch:
        case 1:
            type = input("Enter type (regular or daily wager r|d) : ")
            if type == "r":
                eid, name, basic, da, hra = input(
                    "Enter details\neid,name,basic,da,hra (space seperated) : "
                ).split()
                x = Regular(eid, name, int(basic), int(da), int(hra))
            else:
                eid, name, wage, days = input(
                    "Enter details\neid,name,wage,days (space seperated) : "
                ).split()
                emp = DailyWager(eid, name, int(wage), int(days))
        case 2:
            type = input("Enter type (regular or daily wager r|d) : ")
            if type == "r":
                eid = input("Enter eid : ")
                newsal = input("Enter new salary : ")
                if eid in regular.keys():
                    regular[eid]["salary"] = newsal
            else:
                eid = input("Enter eid : ")
                newsal = input("Enter new salary : ")
                if eid in daily_wager.keys():
                    daily_wager[eid]["salary"] = newsal
            print("Updation sucess\n")
        case 3:
            type = input("Enter type (regular or daily wager r|d) : ")
            if type == "r":
                eid = input("Enter eid : ")
                if eid in regular.keys():
                    del regular[eid]
            else:
                eid = input("Enter eid : ")
                if eid in daily_wager.keys():
                    del daily_wager[eid]
            print("Deletion sucessfull\n")
        case 4:
            eid = input("Enter eid : ")
            if eid in regular.keys():
                print("Found as regular employee \n")
            elif eid in daily_wager.keys():
                print("Found as daily wager \n")
            else:
                print("Not Found\n")
        case 5:
            type = input("Enter type (regular or daily wager r|d) : ")
            print_regular() if type == "r" else print_daily_wager()
        case 6:
            display_departments()
        case 7:
            print("Thankyou")
            break
