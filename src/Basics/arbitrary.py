# *args - pass multiple non key arguments, tuple
# **kwargs - pass multiple keywords arguments, dict

def sum(*args):
    print(type(args))
    total = 0
    for arg in args:
        total+=arg
    return total

print(sum(1,2,3,4,5))

def address(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print( f"{key}: {value}" )


print(address(
    street= "Park Avenue",
    pincode="123455"
))