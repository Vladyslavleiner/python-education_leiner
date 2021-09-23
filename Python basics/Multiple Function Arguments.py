# edit the functions prototype and implementation
def foo(a, b, c, *extra_arguments):
    return len(extra_arguments)

def bar(a, b, c, **extra_arguments):
    if extra_arguments["magicnumber"] == 7:
        return True
    else:
        return False


# test code
if foo(1,2,3,4) == 1:
    print("Good.")
if foo(1,2,3,4,5) == 2:
    print("Better.")
if bar(1,2,3,magicnumber = 6) == False:
    print("Great.")
if bar(1,2,3,magicnumber = 7) == True:
    print("Awesome!")