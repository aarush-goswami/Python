# User define Exception here we define our own type of exception by taking inheritance from exception class


try :
    x= int(input("1 : "))
    y= int(input("2 : "))
    res = x/y
except ZeroDivisionError:
    print("Not divided by 0") #when try fails
except ValueError as ve:
    print(ve) # no exception
else:
    print(res)
finally:
    print("program ends") #executes everytime

'''Rules for Exception Handling
    1 every try block must have atleast 1 except block
    2.We can't place a statement between try & except block
    3.We can attach except blocks with a try block the type of exception first raise by the try bblock will decides the execution relevant
    except block.Only 1 except block will executes and other will be discarded 
'''  
t = tuple([1,0])
print(t[0])