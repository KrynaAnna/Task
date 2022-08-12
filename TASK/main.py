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

# get the average rating of all the movies in which the actor starred
for row in output_table:
    rate_per_actor = []
    for line in data:
        if row[0] in line['stars'].split(', '):
            rate_per_actor.append(float(line['rating']))
    average_rating_per_actor = Decimal(sum(rate_per_actor) / len(rate_per_actor))
    average_rating_per_actor = str(round(average_rating_per_actor, 2))

    # appending average rating per actor to output table
    index_of_row = output_table.index(row)
    output_table[index_of_row].append(average_rating_per_actor)

# sorting output table by the total number of movies and alphabet order
output_table.sort(key=lambda x: (x[-2], x))

# beautiful output
print(tabulate(output_table, headers=['Star Name', 'Movies', 'AVG Rating'], tablefmt="psql", disable_numparse=True,
               colalign=("left", "center", "center")))

'''
# DIFFERENT TABLE OUTPUT OPTION
import sqlite3

# creation table k
connection = sqlite3.connect('../TASK/db.sqlite')
cursor = connection.cursor()
cursor.execute('CREATE table if not exists actors (Star_Name TEXT, Movies TEXT, AVG_Rating TEXT)')

for out in output_table:
    keys = tuple(out)
    print(keys)
    cursor.execute('INSERT INTO actors values(?, ?, ?)', keys)

connection.commit()
connection.close()
'''