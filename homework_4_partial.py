#შექმენით dict -ი 2 ლისტისგან#
keys: list = {'Ten', 'Twenty', 'Thirty'} 
values: list = {10,20,30}
dict = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}


#შეერთება
dict1 = {'Ten' : 10, 'Twenty' : 20, 'Thirty' : 30}
dict2 = {'Thirty' : 30, 'Forty' : 40, 'Fifty' : 50}

dict1.update(dict2)
print(dict1)
#
sampleDict = {
    "class":{
        "student":{
            "name" : "Mike",
            "marks" : {
                "physics": 70,
                "history": 80
            }
        }
    }
}

'''
sampleDict["name"] = "Mike"
sampleDict["marks"] = "physics", "history"
sampleDict["history"] = 80
sampleDict.pop("history")

'''

history_mark = sampleDict["class"]["student"]["marks"].pop("history")
print("Popped history mark:", history_mark)

#
dict = {}
name = input('Please enter your name:')
age = int(input('Please enter your age:'))
address = input('Please enter your address:')

dict['name'] = name.title()
dict['age'] = age
dict['address'] = address
for name, definition in dict.items():
    print(f"{name} : {definition}")

###
cities = [ 
    {'city1': 2000, 
    'city2': 3550, 
    'city3': 25, 
    'city4': 89, 
    'city5': 150}
]

highest_population = cities[0]['city']
