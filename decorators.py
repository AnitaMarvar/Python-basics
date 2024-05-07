#DECORATORS
#timimg function execution
 #write decortaor that measures the time a fucntion takes to execute
import time
def timerr(function):
    def wrapper(*args,**kwargs):
        start = time.time()
        result=function(*args,**kwargs)
        end=time.time()
        print(f"{function.__name__}ran in {end-start} time")
        return result
    return wrapper

@timerr
#kuch bhi timer function se hoke hi jaayega
def example_function(n):
    time.sleep(n)

example_function(3)
# #example_function nhi execute hoga pahele timerr hi execute hoa


#2.debugging function calls
#create a decorator to print the function name and the values of its arguments every time the function is called
def debug(func):
    def wrapper(*args,**kwargs):
        args_value=', '.join(str(arg) for arg in args)
        kwargs_value=', '.join(f"{k}={v}" for k,v in kwargs.items())
        print(f"calling:{func.__name__} with args {args_value} and kwargs {kwargs_value}")
        return func(*args,**kwargs)

    return wrapper  #wrapper return hoga hi
# @debug
def hello():
    print("hello")

@debug 
def greet(name,greeting="hello"):
    print(f"{greeting},{name}")

hello()
greet("chai",greeting="hanji")

#3.Cache return values
#implement a decorator that caches the return values of a function,
#so that when its called with the same arguments the cached 
#value is returned instead of re-executing the function
#deals with memory
import time

def cache(func):
    cache_value={}
    print(cache_value)
    def wrapper(*args):  #can add **kwargs
        if args in cache_value:
            return cache_value[args]
        result=func(*args)
        cache_value[args]=result
        return result
    return wrapper

@cache
def long_running_function(a,b):
    time.sleep(4)
    return a+b
print(long_running_function(2,3))
print(long_running_function(2,3))
print(long_running_function(4,3))
#der baad hi output aayega due to sleep