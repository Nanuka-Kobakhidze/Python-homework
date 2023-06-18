
print("hello")
message = "hello"
print(message)
print(message.upper())
print(f"I am going to say {message}")
#
name = "ada lovelace"
print(name.title())

first_name = "michael"
last_name = "scott"
full_name = f"{first_name} {last_name}"
print(full_name.title())
print(f"Hello, {full_name.title()}")
message = f"Hello, {full_name.title()}"
print(message)
#
print("Python")
print("\tPython")
print("\nPython")

lang = "python "
print(lang)
print(lang.rstrip())

fav_lang = " python "
fav_lang.strip()
print(fav_lang)
print(fav_lang.strip())
#
print(0.1 + 0.1)
print(0.2 + 0.3)
#
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)
#
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.pop()
print(motorcycles)
#
guests = ['lana' , 'mia' , 'ivy' , 'johnny']
print(f"Hello {guests[2]}, seinding an invitation to my dinner party")
print(f"this guest can't make it to dinner: {guests[1]}")
removed = guests.pop(1)
print(guests)
print(removed)
guests.append('moa')
print(guests)
guests.insert(1, 'nunu')
print(guests)
del guests[-1]
print(guests)
#
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
 print(f"{magician.title()}, that was a great trick!")
 print(f"I can't wait to see your next trick, {magician.title()}.\n")
#
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
#
squares = [value**2 for value in range(1, 11)]
print(squares)
#
for number in range(1,21):
   print(number)
#
odd = list(range(1, 21, 2))
for number in odd:
   print(number)
#
nums = [value*3 for value in range(3,31)]
print(nums)

