import requests
from random import choice
from pyfiglet import figlet_format
from termcolor import colored

header = figlet_format("DAD JOKES 2018!")
header = colored(header, color="green")
print(header)

user_input = input("What would you like to search for? ")
url = "https://icanhazdadjoke.com/search"
res = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term":user_input}
).json()

num_jokes = res["total_jokes"]
results = res["results"]
if num_jokes > 1:
   print(f"I FOUND {num_jokes} JOKES ABOUT {user_input}. HERE'S ONE:)
   print(choice(results)["joke"])
elif num_jokes == 1:
   print(f"I FOUND ONE JOKE ABOUT {user_input}")
   print(results[0]['joke'])
else:
   print(f"SORRY, THERE ARE NO JOKES WITH YOUR TERM: {user_input}")
