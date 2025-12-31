import Lab.exp.function as function
import sys
pswd = 1234
st_list = ["Jordy","Nick","Johny"]

p = int(input("Enter password : "))
if p == pswd:
    while True:
        opt = int(input("1.Show students\n2.Search for student\n3.Add student\n4.Delete student\n5.Quit...  "))

        match(opt):
            case 1:
                function.show_user(st_list)
            case 2:
                function.search_student(st_list)
            case 3:
                function.add_student(st_list)
            case 4:
                function.delete_student(st_list)
            case 5:
                sys.exit("Thankyou\n")
else:
    print("Login Failed \n")