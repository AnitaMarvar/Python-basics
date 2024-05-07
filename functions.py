#write function to calculate square of a number
def squared_result(num):
    ans=num*num
    return ans
print(squared_result(4))

#Function with multiple parameters
# take 2 numbers and return their sum
def Addition(num1,num2):
    ans=num1+num2
    return ans

print(Addition(3,5))

#polymorphism in functions
# write a function 'multiply' that multiplies 2 numbers
#but can also accept and multiply strings
#polymorphism-ek cheez anek kaam,here * is used for
#both numbers and strings
#in python operators already have polymorphism property
def Multiply(item1,item2):
    ans=item1 * item2
    return ans
print(Multiply('a',5))
print(Multiply(5,'a'))
# #output - aaaaa for both

#function returns both area and circumference of the circles
#return multiply values
import math
def Area_and_Circum(radius):
    pii = math.pi
    area =  pii * radius * radius
    circumference = 2 * pii * radius
    return area,circumference

# a,c = Area_and_Circum(2)
# print("Area is ",a,"and ","circumference is ",c)
# #output - (12.566370614359172, 12.566370614359172)


# write a function that greets a user.if no name
# is provided, it should greet with a default name
def Greeting(name="User"):
    print("hello",name)
Greeting("Anita")

#lambda function-dunction ka naam nhi hota
#compute cube of a function
cube = lambda x: x **3
print(cube(3))


#function with *args
#write a function that takes variable number of
#arguments and returns their sum
def Sums(*args):
    ans=sum(args)
    print(ans)
Sums(1,2,2,2,1,3)
Sums(1,2)

#function with **kwargs
#create a function that accepts any number of
#keyword parameters and prints them in the format
#key:value 

def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
print_kwargs(name="Shaktimaan",power="lazer")
print_kwargs(name="Shaktimaan")
print_kwargs(name="Shaktimaan",power="lazer",enemy="Ai")


#generate function with yield
#write a generator function that yields even numbers 
#upto a specified limit
def even_num(limit):
    for i in range(2,limit+1,2):
        yield i
for num in even_num(10):
    print(num)

#recursive function
#calulate the factorial of a number
def factorial(num):
   if(num==0):
      return 1
   else:
      return num * factorial(num-1)
factorial(4)

