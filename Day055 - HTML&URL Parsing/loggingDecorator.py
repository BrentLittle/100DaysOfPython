

def loggingDecorator(function):
    def wrapper(*args,**kwargs):
        print(f"You called {function.__name__}")
        result = function(args[0],args[1],args[2])
        print(f"It returned: {result}")
    return wrapper

@loggingDecorator
def aFunction(a,b,c):
    return a*b*c

aFunction(1,2,3)