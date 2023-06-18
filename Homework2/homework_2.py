#conditional_tests
fruit = 'apple'
print(fruit)
print("Is fruit == 'apple' ? I predict True.")
print(fruit == 'apple')

print("\nIs fruit == 'tomato'? I predict False.")
print(fruit == 'tomato')

car = 'Audi'
print("Is car == 'Audi' ?")
print(car == 'Audi')



#tests for equality and inequality
name = 'nanuka'
print(name)
name == 'nanuka'
print(name == 'nanuka')
print(name == 'anuka')

name = 'Nanuka'
print(name == 'nanuka')
print(name.lower() == 'nanuka')

#numerical tests
age = 25
print(age == 25)
print(age == 23)

age = 25
print(age < 100)
print(age > 2)
print(age < 11)
print(age <= 50)

# multiple conditions
age_0 = 14
age_1 = 27
print(age_0 > 8 and age_1 < 30)
print(age_0 < 9 and age_1 > 9)
print(age_0 >=11 or age_1 <= 12)

#lists
fav_games = ['hollow knight' , 'borderlands' , 'skyrim' , 'warframe']
print('warframe' in fav_games)
print('apex' in fav_games)

#if statements
age = 19
if age == 18:
    print("you can vote")

age = 6
if age >= 6:
    print("you are ready to go to school")
else:
    print("you are too young")
age = 3
if age >= 6:
    print("you are ready to go to school")
else:
    print("you are too young")

#Anyone with the score of 95-100 gets first place
#Anyone with the score of 80-95 gets the second place
#Anyone with the score below 80 gets the third place

score = 98
if score > 96:
    print("Congratulations, you got the first place!")
elif score < 95:
    print("Congratulations, you got the second place!")
else:print("Congratulations, you got the third place!")

score = 56
if score > 96:
    print("Congratulations, you got the first place!")
elif score < 95:
    print("Congratulations, you got the second place!")
else:print("Congratulations, you got the third place!")

#kids under 5 can enter freely in the water park
#fee between 5-18 is 20$
#fee for over 18 adults is 45$

age = 4
if age < 5:
    print("your admission fee is 0")
elif age < 18:
    print("your admission fee is 20")
else:
    print("your admission fee is 45")

#alien was just show down in a game.

alien_color = 'green'
if 'green' in alien_color:
    print("you have earned 5 points")
    alien_color = 'red'

alien_color = ['green' , 'red']
if 'green' in alien_color:
    print("you have earned 5 points")
else:
    print("you have earned 10 points")
alien_color = 'yellow'
if 'green' in alien_color:
    print("you have earned 5 points")
else:
    print("you have earned 10 points")

if 'green' in alien_color:
    print("you have earned 5 points")
elif 'red' in alien_color:
    print("you have earned 10 points")
else:
    print("you have earned 15 points")

age = 87
if age < 2:
    print("this person is a baby")
elif age >= 2 and age < 4:
    print("this person is a toddler")
elif age >= 4 and age < 13:
    print("this person is a kid")
elif age >= 13 and age < 20:
    print("this person is a teenager")
elif age >= 20 and age < 65:
    print("this person is an adult")
else:
    print("this person is an elder")

#fav fruits.
favourite_fruits = ['orange' , 'pineapple' , 'cherry']
if 'pineapple' in favourite_fruits:
    print("you have great taste")
if 'orange' in favourite_fruits:
    print("you love Autumn")
if 'cherry' in favourite_fruits:
    print("you like sour food")
if 'kiwi' in favourite_fruits:
    print("this is not in the list")
if 'mango' in favourite_fruits:
    print("you have good tase but it is not in the list")

#usernames, 5.9
usernames = ['tom' , 'admin' , 'kenny' , 'kate' , 'eve']
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else: 
        print("Hello 'tom', thank you for logging in")
        #
usernames = []
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else: 
        print("Hello 'tom', thank you for logging in")
else:
    print("We need to find some users.")

#checking usernames, 5.10
current_users = ['jane' , 'mike' , 'jesse' , 'walt' , 'gus' , 'tony']
new_users = ['nick' , 'Jane' , 'SAM' , 'bob' , 'Tony' , 'Liz']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("Sorry " + new_user + " this name is taken")
    else:
        print("Great " + new_user + " is still available")

#lists products

products = ['apples, 15' , 'butter, 8' , 'milk, 4' , 'coffee, 20' , 'bread, 2']
for product in products:
    print(f"The name and price of this product is: {product}")

###


