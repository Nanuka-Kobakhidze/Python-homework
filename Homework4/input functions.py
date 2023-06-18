prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")
######
#7.1
car = input("Please enter the name of the car you would like to rent: ")
print(f"Let me see if I can find you a {car.title()}")

#7.2
size = input("Please tell us how many people you would like to reserve a table for: ")
size = int(size)
if size > 8 and size != 300:
    print("You will have to wait for a table")
elif size == 300:
 print("This is sparta")
else:
   print('Great, your table is ready!')

###
