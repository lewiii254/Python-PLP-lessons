a = 14
b = 2


try:
    print(a/b)
    k = int(input("Enter a Number: "))
except ZeroDivisionError:
    print("You can't divide this with Zero")
except ValueError:
    print("We have a wrong value")
except Exception:
    print("This is a very Serious Error")
else:
    print("No exceptions occurred!")
finally:
    print("Thank for Banking with Us")
