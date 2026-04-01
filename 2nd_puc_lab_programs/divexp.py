def DivExp(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: both a and b must be numbers."
    return result
a= float(input("Enter the value of a: "))
b= float(input("Enter the value of b: "))
print("The result of a/b is : ", DivExp(a,b))