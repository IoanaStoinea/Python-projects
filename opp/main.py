'''''
The problem: Car Rental Company
Company X has a car rental service. The business knows for each of the 100 cars the following: year model, type
of the car, the price per day and if the car uses petrol or diesel.
a) Identify the class (or classes) that models this situation using the Object-Oriented Paradigm. 
b) Implement the identified class (or classes).
c) Implement the necessary methods to achieve the following:
    i) Introduce new cars for rental. 
    ii) Answer if there is a specific type of car for rental given the type of car. 
    iii) Know the cheapest car in the company.
    iv) Know how many cars of a specific year are available for rent.

In our problem, we have two classes: one to represent the company and the other one to represent cars.
'''''

from enum import Enum

class CarType(Enum):
    SEDAN = 1
    SUV = 2
    BAKKIE = 3


class Fuel(Enum):
    DIESEL = 1
    PETROL = 2

'''''
To implement the class car, we are going to create two extra classes: CarType and Fuel.
According to the problem description, the cars have a type and can only be of three types. 

That is a good indication that we have to use an enum. This “special type of classes” only defines the values 
that can be assigned.

The fuel type is similar. We can have a car that uses diesel or petrol.
That’s another good opportunity to use enums.

'''''
class Car:
    def __init__(self, model_year, type, price_per_day, fuel):
        self.__model_year = model_year
        self.__type = type
        self.__price_per_day = price_per_day
        self.__fuel = fuel

    def get_type(self):
        return self.__type

    def get_price_per_day(self):
        return self.__price_per_day

    def get_model_year(self):
        return self.__model_year

    def __str__(self):
        return '[' + self.__model_year + ', ' + str(self.__type) + ']'

'''''
In this case, the methods that we have to implement should be in the class company. One way to notice that 
all the methods must be implemented in the class Company is to ask ourselves what data we need to implement 
the methods.

For instance, to answer the question “is there a specific type of car for rental given the type of car?”, 
we need to check all the cars the company have. 

Where are all the cars stored? 

They are in the class Company. So we have to implement this method in the class Company. 
You can use similar thinking with the rest of the questions.
'''''
class CompanyX:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def is_there_a_specific_type_of_car(self, type):
        for car in self.cars:
            if car.get_type() == type:
                return True
        return False

    def cheapest_car(self) -> Car:
        cheapest = self.cars[0]
        for i in range(1, len(self.cars)):
            if self.cars[i].get_price_per_day() < cheapest.get_price_per_day():
                cheapest = self.cars[i]
        return cheapest

    def how_many_car_from_specific_year_are_available(self, year):
        counter = 0
        for car in self.cars:
            if car.get_model_year() == year:
                counter += 1
        return counter
'''''
Basic algorithms used in the previous implementation
1.is_there_a_specific_type_of_car: In this method a simple search was used. We iterated over all the elements of
                                   the collection or array, when we found the type of car we were looking for, 
                                   we return a result.
                                   
2.cheapest_car: A basic algorithm for finding a minimum. In this case, we assume the first element of the 
              collection is the minimum (the cheapest car in this case), then we go through the rest of the 
              elements of the collection, and if we find a car that is cheaper than the one we assumed is the 
              cheapest one, we update the cheapest car.
              
3.how_many_car_from_specific_year_are_available: A basic algorithm for counting. We iterate over the elements of
                                                 the array. If the current car has the same year model as the 
                                                 parameter of the method, we count.
'''''


'''''
Now is time to create a console app so we can put our code to work.
First, we create an object of type CompanyX. This object will represent the company and, it will be the 
entry point to our code.

Then we create three cars (it can be more) and add them to the company using the corresponding method.
Now we can use the other methods we implemented. 

The company has three cars. It is time to use the methods we implemented:
    -if there is a car of a certain type
    -what is the cheapest car (according to the rental price)
    -the total of cars that have a specific year model.
'''''



if __name__ == '__main__':
    company = CompanyX()

    car1 = Car('2010', CarType.SEDAN, 25.0, Fuel.DIESEL)
    car2 = Car('2011', CarType.SEDAN, 22.0, Fuel.PETROL)
    car3 = Car('2010', CarType.BAKKIE, 35.0, Fuel.DIESEL)

    company.add_car(car1)
    company.add_car(car2)
    company.add_car(car3)

    print('Is there a bakkie: ', company.is_there_a_specific_type_of_car(CarType.BAKKIE))
    print('Is there a SUV: ', company.is_there_a_specific_type_of_car(CarType.SUV))
    print('Is there a sedan: ', company.is_there_a_specific_type_of_car(CarType.SEDAN))

    print('The cheapest car is ', company.cheapest_car())

    print('Total of cars from 2010: ', company.how_many_car_from_specific_year_are_available('2010'))
    print('Total of cars from 2011: ', company.how_many_car_from_specific_year_are_available('2011'))
    print('Total of cars from 2012: ', company.how_many_car_from_specific_year_are_available('2012'))