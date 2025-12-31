num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))

def add(num1,num2):
    return num1 + num2
def sub(num1,num2):
    return num1-num2
def div(num1,num2):
    return num1//num2
def mul(num1,num2):
    return num1*num2

opr = input("Enter the operator : (+ , - , // , * ) : ")
match (opr): 
    case  "+":
        res = add(num1,num2)
        print("sum = ",res)
    case "-":
        res = sub(num1,num2)
        print("subtraction = ",res)
    case "//":
        if (num2 ==0):
            print("Infinity\n")
        else:
            res = div(num1,num2)
            print("Division = ",res)
    case "*":
        res = mul(num1,num2)
        print("Multiplication = ",res)