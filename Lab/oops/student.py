class Student:
    def __init__(self, Croom, sub : list[str]):
        self.Croom = Croom
        self.sub = sub

    def accept(self, name : str, rno, mno):
        self.name = name
        self.rno = rno
        self.mno = mno

    def display(self):
        print(
            f"Name : {self.name}\nRoll No : {self.rno}\nMobile No. : {self.mno}\nClassroom : {self.Croom}\nSubjects : {self.sub}"
        )


R = Student(690, ["CS", "DBMS", "NK"])
R.accept("Raju",69,9999888065)
R.display()