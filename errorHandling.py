a = 7
b = 2

# print(a/b)
try:

    print(a/b)
    k = int(input("Enter a Number: "))
except ZeroDivisionError:
    print("You cant divide this with Zero")
except ValueError:
    print("We have a wrong value")
except Exception:
    print("This is a very Serious Error")
finally:
    print("Thank for Banking with Us")