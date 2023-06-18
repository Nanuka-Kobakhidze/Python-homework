alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
#6.1 printing each of the values
person = {
    'first_name': 'katherine',
    'last_name': 'pierce',
    'age': 24,
    'city': 'Boston',
}
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])
#6.2
fav_numbers = {'Ann':5, 'Scott':12, 'Mia':3, 'Ivy':8, 'John':25}
print(fav_numbers)
#6.4
python_terms = {
    'loop':'can iterate through lists',
    'string':'series of characters',
    'append':'adding an element into the list'
}
print("These are the few terms I learned in Python:")
for key in python_terms.keys():
    print(key.title())
#6.5
rivers = {
    'nile':'egypt',
    'amazon':'america',
    'yangtze':'china'
}
for key, value in rivers.items():
    print(f'\n The {key.title()} runs through {value.title()}')
#6.6
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
people = ['jen', 'sarah', 'jim', 'edward', 'phil', 'ash']
for person in people:
    if person in favorite_languages:
        print(f'Thank you {person.title()} for taking the poll')
    else:
        print(f'Please take the poll first, {person.title()}')
#6.7
people = [
     {
    'first_name': 'katherine',
    'last_name': 'pierce',
    'age': 24,
    'city': 'Boston',
},
{
    'first_name': 'jack',
    'last_name': 'white',
    'age': 43,
    'city': 'ny'
},
{
    'first_name': 'alex',
    'last_name': 'gilbert',
    'age': 19,
    'city': 'seattle'
}
]
for person in people:
    print(person)
    ## or
for person in people:
    for key, value in person.items():
        print(f"{key.title()}: {value}")
###6.8
pets = [
    {
        'animal':'dog',
        'owner':'ash'
    },
    {
        'animal':'cat',
        'owner':'alison' 
    },
    {
        'animal':'owl',
        'owner':'kate' 
    }
]
for pet in pets:
    animal = pet['animal']
    owner = pet['owner']
    print(f"{owner.title()}'s pet is {animal.title()}")

###6.9
favourite_places = {
    'jack':['cemetrty', 'school', 'gym'],
    'wendy':['beach', 'pizzeria'],
    'kenny':['prison', 'mall', 'woods']
}
for key,value in favourite_places.items():
    print(f"{key.title()}'s favourite places are: {value}")
##6.10
fav_numbers = {
    'Ann':[5, 8],
    'Scott':[12,13,14], 
    'Mia':[3,9], 
    'Ivy':[8,5,12],
    'John':[25,99]
}
for name, number in fav_numbers.items():
    print(f"favourite numbers:{number}, name: {name.title()}")
###