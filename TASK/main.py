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

# output table
output_table = []

# get the number of movies per actor
for actor in unique_actor_names:
    number_movies_per_actor = actor_names.count(actor)
    if number_movies_per_actor >= 2:
        output_table.append([actor, number_movies_per_actor])
