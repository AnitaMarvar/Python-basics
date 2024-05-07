#1. create a car class with attributes/variables like brand
#and model then create an instance of class
class Car:
   def __init__(self,userbrand,usermodel):
     self.brand=userbrand
     self.model=usermodel

my_car = Car("Toyota","Corolla")
print(my_car.brand)
print(my_car.model)


#2. add a method to car class that displays the full name of the car(brand and model)
class Car:
   def __init__(self,userbrand,usermodel):
      self.userbrand=userbrand
      self.usermodel=usermodel

   def fullname(self):
      print("car is",self.userbrand,"from",self.usermodel)
mycarmodel = Car("thar","mahindra").fullname()

#inheritance
#3. create ElectricCar class inherits from the car class and has an additional 
#attribute battery,size
class ElectricCar(Car):
   def __init__(self,brand,model,battery_size):
      super().__init__(brand,model)
      self.battery_size=battery_size
      

electricCar=ElectricCar("Tesla","Model S","85kwh")
print(electricCar.usermodel)


# Encapsulation

#4. modify the car class to encapsulate the brand attribute making it private and provide a getter method for it
#brand encapsulate hona chahiye main chahu toh pata lage warna nhi
class Car:
   def __init__(self,brand,model):
      self.__brand=brand
      self.usermodel=model
   def get_brand(self):
      return self.__brand +" !"

   def fullname(self):
      print("car is",self.userbrand,"from",self.usermodel) 
print(Car.__brand)

#polymorphism
#4. demostrate polymorphism by defining a method furl_type in both car and eelectricCar classes but with different
#behaviours
class Car:
   def __init__(self,userbrand,usermodel):
      self.userbrand=userbrand
      self.usermodel=usermodel

   def fullname(self):
      print("car is",self.userbrand,"from",self.usermodel)
   def fuel_type(self):
      return "Petrol or Diesel"
   
class ElectricCar(Car):
   def __init__(self,brand,model,battery_size):
      super().__init__(brand,model)
      self.battery_size=battery_size
   def fuel_type(self):
      return "Electric charge"
      
mytesla = ElectricCar("tesla","model S","85kwh")
print(mytesla.fuel_type())
safari = Car("Tata","Safari")
print(safari.fuel_type())


#class variables 
# 5. add a class variable to car that keeps track of the number od cars created
class Car:
   total_car=0
   def __init__(self,userbrand,usermodel):
      self.userbrand=userbrand
      self.usermodel=usermodel
      Car.total_car +=1
      # jitni baar bhi call kiya toh init execute hoga 
      #therefore udhar hi +1 kar diya
      #kitne objects banaye yeh batatyega 

   def fullname(self):
      print("car is",self.userbrand,"from",self.usermodel)
   def fuel_type(self):
      return "Petrol or Diesel"
   
class ElectricCar(Car):
   def __init__(self,brand,model,battery_size):
      super().__init__(brand,model)
      self.battery_size=battery_size
   def fuel_type(self):
      return "Electric charge"
      
mytesla = ElectricCar("tesla","model S","85kwh")
print(mytesla.fuel_type())
safari = Car("Tata","Safari")
print(safari.fuel_type())
print(safari.total_car)

#static method
#6. add static method to the car class that returns the
#general description of the car
class Car:
   total_car=0
   def __init__(self,userbrand,usermodel):
      self.userbrand=userbrand
      self.usermodel=usermodel
      Car.total_car +=1
      # jitni baar bhi call kiya toh init execute hoga 
      #therefore udhar hi +1 kar diya
      #kitne objects banaye yeh batatyega 
   # staticmethods-is a method that belongs to the class
   #rather than instance of a class,
   #for static method no need for self
   #it should not be accessed by objects

   @staticmethod
   def general_description():
      return "Cars are means of transport"
   

   def fullname(self):
      print("car is",self.userbrand,"from",self.usermodel)
   def fuel_type(self):
      return "Petrol or Diesel"
   
class ElectricCar(Car):
   def __init__(self,brand,model,battery_size):
      super().__init__(brand,model)
      self.battery_size=battery_size
   def fuel_type(self):
      return "Electric charge"
      
mytesla = ElectricCar("tesla","model S","85kwh")
print(mytesla.fuel_type())
safari = Car("Tata","Safari")
print(safari.fuel_type())
print(safari.total_car)
print(Car.general_description())

#decorators
#6. use property decorator in the Car class to make 
#the model attribute read only
class Car:
   total_car=0
   def __init__(self,brand,model):
      self.brand=brand
      self.__model=model
      Car.total_car +=1
     

   @staticmethod
   def general_description():
      return "Cars are means of transport"
   

   def fullname(self):
      print("car is",self.brand,"from",self.model)
   def fuel_type(self):
      return "Petrol or Diesel"
   @property
   #@property-aisi koi property hai joh sab access nhi kar sakte
   #agar acess karna ho toh mere method ke through access karna hoga
   #helps in read only feature
   #first make the attribute privateand then use property and add a method
   
   def model(self):
      return self.__model
   
class ElectricCar(Car):
   def __init__(self,brand,model,battery_size):
      super().__init__(brand,model)
      self.battery_size=battery_size
   def fuel_type(self):
      return "Electric charge"
      
mytesla = ElectricCar("tesla","model S","85kwh")
print(mytesla.fuel_type())
safari = Car("Tata","Safari")
print(safari.fuel_type())
print(safari.total_car)
print(Car.general_description())
# mytesla.__model="Nexon"
print(mytesla.model)

#class inheritance and isinstance() function
#demonstrate the use of isinstance()to check if my_tesla is an instance of Car or Electric Car
class Car:
   total_car=0
   def __init__(self,brand,model):
      self.brand=brand
      self.__model=model
      Car.total_car +=1
     

   @staticmethod
   def general_description():
      return "Cars are means of transport"
   

   def fullname(self):
      print("car is",self.brand,"from",self.model)
   def fuel_type(self):
      return "Petrol or Diesel"
   @property
   #@property-aisi koi property hai joh sab access nhi kar sakte
   #agar acess karna ho toh mere method ke through access karna hoga
   #helps in read only feature
   #first make the attribute privateand then use property and add a method
   
   def model(self):
      return self.__model
   
# class ElectricCar(Car):
#    def __init__(self,brand,model,battery_size):
#       super().__init__(brand,model)
#       self.battery_size=battery_size
#    def fuel_type(self):
#       return "Electric charge"
      
# mytesla = ElectricCar("tesla","model S","85kwh")
# # print(mytesla.fuel_type())
# # safari = Car("Tata","Safari")
# # print(safari.fuel_type())
# # print(safari.total_car)
# # print(Car.general_description())
# # # mytesla.__model="Nexon"
# # print(mytesla.model)

#only here is isinstance()
# print(isinstance(mytesla,Car))
# print(isinstance(mytesla,ElectricCar))

#multiple inheritance
#create 2 classes Battery and Engine and let the ElecricCar
#class inherit from demonstrating mutilple inheritance
class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "this is engine"

class ElectricCar2(Battery,Engine,Car):
    pass

my_new_tesla=ElectricCar2("tesla","electric")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())