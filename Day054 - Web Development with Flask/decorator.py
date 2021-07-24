import time


def delayDecorator(function):
    def wrapperFunction():
        time.sleep(2)
        # Do something before
        function()
        # Do something after
    return wrapperFunction


@delayDecorator
def sayHello():
    print("Hello")

@delayDecorator
def sayBye():
    print("Bye")

def sayGreeting():
    print("How are you today?")

# sayHello()
# sayBye()
# sayGreeting()

# decoratedFunc = delayDecorator(sayGreeting)
# decoratedFunc()





current_time = time.time()

def speedCalcDecorator(function):
    def wrapper():
        start=time.time()
        function()
        end=time.time()
        print(f"{function.__name__} run time: {end-start}s")
    return wrapper

@speedCalcDecorator
def fastFunction():
    for i in range(10000000):
        i * i
        
@speedCalcDecorator
def slowFunction():
    for i in range(100000000):
        i * i


fastFunction()
slowFunction()