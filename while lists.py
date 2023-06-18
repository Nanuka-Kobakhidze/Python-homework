##7.8, 7.9
sandwich_orders = ['philly', 'grilled cheese', 'pastrami', 'pastrami', 'avocado', 'pastrami', 'bacon and cheese']
finished_sandwiches = []

print('\nWe have run out of pastrami')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwiches = sandwich_orders.pop()
    print(f'\nMaking your {sandwiches.title()} sandwich')
    finished_sandwiches.append(sandwiches)

print(f'\nFinished making your sandwiches!: ')
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
###
##7.10
responses = {}

polling_active = True

while polling_active:
    vacation = input('\nIf you could visit one place in the world, where would you go? ')
    age = input('\nHow old are you?')
    responses[age] = vacation

    repeat = input('Would you like the other person to respond? (Yes/No)')
    if repeat != "yes":
        polling_active = False

print("\n--- Poll Results ---")
for age, vacation in responses.items():
    print(f"{age} would like to visit {vacation}.")
##