from student import Student
import os
student_list = []

while True:
    print("=" * 40)
    print("***Student Management System***")
    print("=" * 40)

    user_choice = int(
        input(
            f"\n1.Add student\n2.View students\n3.Search Student\n4.Update Marks\n5.Delete Student\n6.Show Topper\n7.Exit\t"
        )
    )
    match user_choice:
        case 1:
            try:
                roll_no = int(input("Enter Roll number : "))
                for student in student_list:
                    if student.roll_no == roll_no:
                        raise Exception("Error : duplcate Roll numbers not allowed")
                name = input("Enter name : ")
                marks = float(input("Enter Marks : "))
                if marks < 0 or marks > 100:
                    raise Exception("Marks should be in range 0 - 100")
                obj = Student(roll_no, name, marks)
                student_list.append(obj)
                obj.calculate_grade()
                print(f"\n{obj.name} added successfully\n")
            except Exception as e:
                print(f"Error : {e}")
        case 2:
            if student_list:
                for student in student_list:
                    student.display()
            else:
                print("No student :( \n")
            print("\n")
        case 3:
            roll_no = int(input("Enter Roll number : "))
            for student in student_list:
                if student.roll_no == roll_no:
                    print(student.display())
                    print("\n")
            else:
                print("Error ! Student Not Found\n")
            print("\n")
        case 4:
            roll_no = int(input("Enter Roll number : "))
            for student in student_list:
                if student.roll_no == roll_no:
                    marks = float(input("Enter Marks : "))
                    if marks < 0 or marks > 100:
                        raise Exception("Marks should be in range 0 - 100")
                    else:
                        student.marks = marks
                        print("Updated Successfully")
                        break
            else:
                print("Error !! Student Not Found\n")
            print("\n")
        case 5:
            roll_no = int(input("Enter Roll number : "))
            for student in student_list:
                if student.roll_no == roll_no:
                    student_list.remove(student)
                    print("Deletion Sucessful")
                    break
            else:
                print("Student not Found")
            print("\n")
        case 6:
            try:
                topper_marks = max(student.marks for student in student_list)
                toppers = [
                    student for student in student_list if student.marks == topper_marks
                ]
                for student in toppers:
                    student.display()
                print("\n")
            except Exception:
                print("Error : Unable to retreive information\n")
        case 7:
            print("\nThanks! Please Visit Again\n")
            break
