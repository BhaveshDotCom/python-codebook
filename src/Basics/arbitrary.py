# *args - pass multiple non key arguments, tuple
# **kwargs - pass multiple keywords arguments, dict

def sum(*args):
    total = 0
    for arg in args:
        total+=arg
    return total

print(sum(1,2,3,4,5))
