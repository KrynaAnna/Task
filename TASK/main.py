import json
from decimal import Decimal
from tabulate import tabulate

# read json
data = json.load(open('data.json'))

# get all actor names from all movies
actor_names = str()
for line in data:
    actor_names += line['stars']

# get only unique names of actors
actor_names = actor_names.split(', ')
unique_actor_names = set(actor_names)
