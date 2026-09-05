# Demonstrate the use of function docstring


def myFunction(arg1, arg2=None):
    """myFunction(arg1, arg2=None) --> Doesn't do anything it just prints 
    
    Parameters:
    arg1: the first argument whatever you like to passing.
    arg2: second argument. Default is None.
    """
    print(arg1, arg2)


def main():
    print(myFunction.__doc__)


if __name__ == '__main__':
    main()