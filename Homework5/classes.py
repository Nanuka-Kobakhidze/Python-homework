class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
def sit(self):
    print(f"{self.name} is now sitting")
def roll_over(self):
    print(f"{self.name} rolled over")
my_dog = Dog('Max', 3)
print(f"my dog's name is {my_dog.name}")
print(f"my dog is {my_dog.age} years old")
my_dog.name

#9.1
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(f"Restaurant name is {self.restaurant_name}")
        print(f"Cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"The {self.restaurant_name} is now open")

my_restaurant = Restaurant('Subway', 'Sandwiches')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

#9.3
class User:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name 
        self.last_name = last_name
        self.age = age 
        self.gender = gender
    
    def describe_user(self):
        print(f"This user's name is {self.first_name}")
        print(f"This user's last name is {self.last_name}")
        print(f"This user's age is {self.age}")
        print(f"This user's gender is {self.gender}")

    def greet_user(self):
        print(f"Hello, {self.first_name}, nice to meet you!")

users = User('Cassy', 'Pierce', '19', 'female' )
users.describe_user()
users.greet_user()



        
