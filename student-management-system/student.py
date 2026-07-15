class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if 90 <= self.marks <= 100:
            self.grade = "A+"
        elif 80 <= self.marks <= 89:
            self.grade = "A"
        elif 70 <= self.marks <= 79:
            self.grade = "B"
        elif 60 <= self.marks <= 69:
            self.grade = "C"
        elif 40 <= self.marks <= 59:
            self.grade = "D"
        else:
            self.grade = "Fail"

    def display(self):
        print(
            f"\n\nRoll : {self.roll_no}\nName : {self.name}\nMarks : {self.marks}\nGrade : {self.grade}\n\n"
        )
