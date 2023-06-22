def greet_user():
    print("Hello!")

greet_user()

#

def greet_user(username):
 """Display a simple greeting."""
 print(f"Hello, {username.title()}!")

greet_user('jesse')

#8.1
def display_message():
   print('I am learning about functions in this chapter')

display_message()

#8.2
def favourite_book(title):
   print(f"one of my favourite books is {title.title()}")

favourite_book('pride and prejudice')

#8.3
def make_shirt(size, text):
   print(f"the size of the tshirt is {size} and its text is {text.title()}")

make_shirt('S', 'blank')
make_shirt(text='blank', size='S')

#8.3
def make_shirt(size='L', text='I love Python'):
   print(f"the size of the tshirt is {size} and its text is {text.title()}")

make_shirt(size='M')

#8.4
def describe_city(city, country='georgia'):
   print(f'{city.title()} is in {country.title()}')

describe_city('tbilisi')
describe_city('riga', country='Latvia')

#8.6
def city_country(city, country):
   info = f'{city}, {country}'
   return info.title()

full_name = city_country('santiago', 'chile')
print(full_name)

#8.7
def make_album(artist, album):
   info = {'artist_name': artist.title(),  'album_name': album.title()}
   return info
musician = make_album('lana del rey', 'ultraviolence')
print(musician)

