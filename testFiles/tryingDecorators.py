def func1(func2):
    print("Before executing the passed function")
    func2()
    print("After executing the passed function")

@func1
def simple_print():
    print("Hello world")


##Visualizing client.event (initial theory)



#check=func1(simple_print) If I just put @func1 above simple_print the it gets passed as argument to func1 that is decorators 
           