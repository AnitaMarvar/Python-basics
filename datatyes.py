#Age Group Categorization
age = int(input("Enter you age: "))
if age<13:
    print("Child")
elif age>13 and age<19:
    print("Teenager")
elif age>20 and age<59:
    print("Adult")
else:
    print("Senior")

#Ticket pricing 
# if 18 and over ticket is for 12$ , 8$ for children,if wednsday discount of 2$
day="Wednesday"
age=26
price=0
if age >=18: 
    price=12
else:
    price=8

if day=="Wednesday":
    price=price-2
print("Ticket price is",price)
# Grade calculator
score=90
if score>=101:
    print("Please verify the grade")
    exit()

if score>=90 and score<=100:
    print("A")
elif score>=80 and score <=89:
    print("B")
elif score>=70 and score<=79:
    print("C")
elif score >=60 and score<=69:
    print("D")
else:
    print("F")


#Fruit ripeness checker
fruit="Banana"
ripeness="Brown"
if fruit=="Banana":
   if ripeness=="Green":
    print("unripe")
   elif ripeness == "Yellow":
    print("Ripe")
   elif ripeness == "Brown":
    print("Overripe")
   else:
     print("Not banana")


weather = "Rainy"
if weather=="Sunny":
    print("go for a walk")
elif weather =="Rainy":
    print("read a book")
elif weather=="Snowy":
    print("Build a snowman")
else:
    print("Do Nothing")
 

distance = 2
if distance<3:
    print("Walk")
elif distance>=3 and distance<=15:
    print("Bike")
else:
    print("car")
  

size="Small"
extra_shot = True
if extra_shot:
    #coffee = size + "coffee with extra shot" sirf yeh bhi chalega 
    if size=="Small":
        print("Your order says small and extra shot of espresso")
    elif size=="Medium":
        print("Your order says medium and extra shot of espresso")
    else:
        print("Your order says Large and extra shot of espresso")
else:
    if size=="Small":
        print("Your order says small ")
    elif size=="Medium":
        print("Your order says medium ")
    else:
        print("Your order says Large ")

password="Anita123"
lengthOfPassword = len(password)
if lengthOfPassword <6:
    print("weak")
elif lengthOfPassword>=6 and lengthOfPassword<=10:
    print("medium")
else:
    print("Strong")

# leap year checker
year=2023
if (year%4==0 and year%100!=0 )or (year%400==0):
    print(year,"Its a leap year")
else:
    print(year,"not a leap year")

#LOOPS
# counting positive numbers
numbers =[1,-2,3,-4,5,6,-7,-8,9,10]
positive_number_counter=0
for number in numbers:
    if number>0:
        positive_number_counter=positive_number_counter+1
print("number of positive numbers",positive_number_counter)

#Sum of even numbers till n
n=10
sum_of_even=0
i=1
while(i<=n):
    if(i%2==0):
        sum_of_even=sum_of_even+1
    i=i+1
print("Count is",sum_of_even)
# or
for i in range(1,n+1):
    if (i%2==0):
        sum_of_even=sum_of_even+1
print("SUm is",sum_of_even)

#print multiplication table for a given num upto 10 but skip the fifth iteration
num=2
ans=0
for i in range (1,11):
    if(i==5):
        continue
    ans = num * i
    print(num,"X",i,"=",ans)


#print reverse of the string using loop
word="LOOP"
reversed_str=""
for i in word:
    reversed_str=i+reversed_str
print(reversed_str)

#find the first non-repeated char
input_str="teeter"
for char in input_str:
    ans=input_str.count(char)
    if(ans==1):
        print(char)
        break   #agar ans mila toh break karo
    

#factorial
num=4
ans=1
i=1
while(i<=num):
    ans = ans*i
    i=i+1
print(ans)

#keep asking the user for input until they enter a number between 1 and 10
num=int(input("enter the number"))
while(num):
    num=int(input("enter the number"))
    if(num>=1 and num<=10):
        break

#check if number is a prime number
num=2
for i in range(2,num):
    if((num%i)==0):
        print(num,"Not a Prime number")
        break
print(num,"is a prime number")

#list uniqueness checker
#check if all the elements are unique,if duplicate 
#is found exit the loop and print the duplicate
items=["apple","banana","orange","apple","Mango"]
for item in items:
    if items.count(item)>1:
        print("Duplicate item is",item)
        break
    else:
       print("NO duplicates")

#implement an exponenetial backoff strategy that doubles the 
#wait time between retry,starting from 1 sec,but
# stops after 5 retry
import time
wait_time=1
max_retries=5
attempts=0
while attempts<max_retries:
    print("Attempt",attempts+1,"wait time:",wait_time)
    time.sleep(wait_time)
    wait_time *=2
    attempts += 1