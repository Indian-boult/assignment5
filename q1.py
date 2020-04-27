def exception_fun(a,b):
    try:
        (a/b)
    except ZeroDivisionError as ve:
        print("We are getting zero division error")

print(exception_fun(5,0))

