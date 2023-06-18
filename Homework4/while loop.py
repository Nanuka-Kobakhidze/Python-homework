###7.4

topping = "Please enter your topping: "
topping +="Enter 'quit' to complete order. "
message = ""
while message != "quit":
    message = input(topping)
    if message != "quit":
        print(f"Adding {message} to yout pizza")
#######
'''
while True:
  topping = input('Please enter the toppings you would like to add to your pizza: ')
  topping += 'Enter quit to complete order'
  while topping != quit:
   break
  print(f"'Adding topping {topping}'")
'''

    