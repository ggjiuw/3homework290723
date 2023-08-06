from pywebio.input import input as pw_input
from pywebio.output import put_success, toast

user_fav_food = pw_input('Enter your favorite food').lower()
print(user_fav_food)

put_success(f'Your favorite food is: {user_fav_food}\U0001F60E')
toast(f'Oh, I also love {user_fav_food}\U0001F609 ')
