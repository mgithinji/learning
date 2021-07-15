# Learning about classes...

# creating a class
class Dog:
    # class attribute
    is_canine = True

    # instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # special instance method for a Pythonic way of printing
    # the instance's description. Can be used instead of the 
    # 'description' instance method created below
    def __str__(self) -> str:
        return '{} is a {} year old dog.'.format(self.name, self.age)

    # instance method. Better to use the dunder __str__ instance method
    # above
    def description(self):
        return '{} is a {} year old dog.'.format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return '{} says {}'.format(self.name, sound)

# class instances of 'Dog'
buddy = Dog('Buddy', 9)
miles = Dog('Miles', 4)

# function to print the 'Dog' class attributes
def print_dog_attributes(dog):
    print('Name: {}'.format(dog.name))
    print('Age: {}'.format(dog.age))
    print('Canine: {}\n'.format(dog.is_canine))

# calling my print_dog_attributes function
print('Printing my \'Dog\' instances: \n')
print_dog_attributes(buddy)
print_dog_attributes(miles)

# changing instance attributes
buddy.age = 10
miles.is_canine = False

# calling my print_dog_attributes function
# after changing instance attributes
print('Printing my \'Dog\' instances, after changing instance attributes: \n')
print_dog_attributes(buddy)
print_dog_attributes(miles)

# printing dog's description from the instance method
print('Printing description of \'Dog\' from the instance method: \n')
print(buddy.description())
print(miles.description())
print('\n')

# making dog speak
print('Calling the instance method to make \'Dog\' speak: \n')
print(buddy.speak('Woof Woof!'))
print(miles.speak('rrrrRRR!'))
print('\n')

# printing dog's description from the dunder .__str__() instance method
print('Printing description of \'Dog\' from the .__str__() instance method: \n')
print(buddy)
print(miles)
print('\n')