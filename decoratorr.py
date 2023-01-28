def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        print(func.__name__)
        if b == 0:
            print("Whoops! cannot divide")
            return # the divide will not be call
        return func(a, b)
    return inner

def type_check(func):
    def inner(*args):
        print(args)
        for n in args:
            if type(n) is not int:
                print(f"Function {func.__name__} shuold get numbers only")
                n=1
            else:
                n=1
                print(func.__name__)
    return inner



@type_check
# @smart_divide
def divide(a, b):
    print(a/b)

divide(10,2)