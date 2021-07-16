"""
Create a Car class with two instance attributes:

.color, which stores the name of the car’s color as a string
.mileage, which stores the number of miles on the car as an integer

Then instantiate two Car objects—a blue car with 20,000 miles and 
a red car with 30,000 miles—and print out their colors and mileage. 
Your output should look like this:

The blue car has 20,000 miles.
The red car has 30,000 miles.

"""

# creating the 'Car' class
class Car:
    
    # class attribute
    vehicle_type = 'car'
    
    # instance attributes
    def __init__(self, color, mileage) -> None:
        self.color = color
        self.mileage = mileage

    # dunder instance method .__str__()
    def __str__(self) -> str:
        return 'The {} {} has {:,} miles.'.format(self.color, self.vehicle_type, self.mileage)

# class instances
prius = Car('blue', 20000)
accord = Car('black', 30000)

print(prius)
print(accord)