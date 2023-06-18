##7.5
active = True
while True:
 age = input('Please enter your age to see the ticket price: ')
 age = int(age)
 if age < 3:
    print('Your ticket price is 0$')
    active = False
 elif age > 3 and age < 12:
    print('Your ticket price is 10$')
    active = False
 else:
    print('Your ticket price is 20$')
    active = False
##
