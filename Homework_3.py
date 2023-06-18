# 1. list ეწოდება ელემენტების გაერთიანებას რომელთა მნიშვნელობის შეცვლაც შეგვიძლია.
# 2. ელემენტი ეწოდება list-ში შემავალ საგნებს.
# 3. list-ის ელემენტს რომ მივწვდეთ უნდა გამოვიყენოთ ინდექსი, მაგალითად დავპრინტავთ ლისტის სახელს, და [] - ში ჩავწერთ სასურველ ინდექსს.

# 4
usernames = ["Nick" , "Theo" , "Theodor" , "Mary" , "nana" , 'manana']
for username in usernames:
    print(username.upper())

# 5
nums = list(range (1,101))
prime_nums = [
    num
    for num in nums
    if num % num != 0
]
print(nums)

# 6
products = [
    ["Google Pixel 7", 1000],
    ["Chevy Volt 2019", 15000],
    ["Macbook Pro M2", 3499],
    ["Microsoft Surface Pro 2", 4649]
]

for i, product in enumerate(products):
    print(f"[{i}] {product[0]} - {product[1]}")

chosen_product = input("Choose Product: ")

product_to_purchase = None
if chosen_product.isdigit():
    chosen_product = int(chosen_product)
    if chosen_product <= len(products):
        product_to_purchase = products[chosen_product]

if product_to_purchase is None:
    print("Selected product does not exist")
else:
    print(f"You have chosen {product_to_purchase[0]} , price: {product_to_purchase[1]} USD")

#ვქმნით ცვლადს რომელშიც შეგვყავს პროდუქტები. გავაკეთეთ პროდუქტების სია სადაც შედის 8 ელემენტი, str და int-ებისგან შემდგარი. 
#შემდგომ გამოვიყენეთ გადანომრვის ფუნქცია და for ციკლი, i-ს გამოყენებით გაკეთდა დანომრილი პროდუქტების სია თანმიმდვრობით, 


#7 იპოვეთ პროდუქტი სახელის მიხედვით

products = [
    ["Google Pixel 7", 1000],
    ["Chevy Volt 2019", 15000],
    ["Macbook Pro M2", 3499],
    ["Microsoft Surface Pro 2", 4649]
]

for i, product in enumerate(products):
    print(f"[{i}] {product}")

chosen_product = input("Choose Product: ")

for chosen_product in products:
    print(f"showing results for {product}")
else:
    print("error, please try again")

#...

users = [
   ["Legend27", "a1s2d3f4"],
   ["james123", "c5bt43f4"],
   ["DaveIsGreat", "wlervtb3r"] 
]

username = input("username: ")
password = input("password: ")

for user in users:
    if user[0] == username and user[1] == password:
        print("Login successful!")
    else:
        print("Login failed.")
        quit()
        

#...................................

products = [
    ["Google Pixel 7", 1000],
    ["Chevy Volt 2019", 15000],
    ["Macbook Pro M2", 3499],
    ["Microsoft Surface Pro 2", 4649]
]

users = [
   ["Legend27", "a1s2d3f4"],
   ["james123", "c5bt43f4"],
   ["DaveIsGreat", "wlervtb3r"] 
]

chosen_product = input("Choose Product: ")

product_to_purchase = None
for product in products:
    if product in products:
        product_to_purchase == products[chosen_product]


if product_to_purchase is None:
    print("Selected product does not exist")
else:
    print(f"You have chosen {product_to_purchase[0]} , price: {product_to_purchase[1]} USD")

username = input("username: ")
password = input("password: ")

for user in users:
    if user[0] == username and user[1] == password:
        print("Login successful!")
    else:
        print("Login failed.")
        quit()



