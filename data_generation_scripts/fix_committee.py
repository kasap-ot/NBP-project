import psycopg2
import random


inserted_pairs = {
    '0-0',
}

def unique_combo() -> list:
    org_id = random.randint(1, 10)
    country_id = random.randint(1, 197)
    new_combination = f'{org_id}-{country_id}'
    
    while (new_combination in inserted_pairs):
        org_id = random.randint(1, 10)
        country_id = random.randint(1, 197)
        new_combination = f'{org_id}-{country_id}'
    
    return [org_id, country_id]


conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="NBP",
    user="nbp_user",
    password="^@sp1r35!"
)

cur = conn.cursor()

query = 'select count(*) from nbp_project.committee'
cur.execute(query)
result = cur.fetchall()

for row in result:
    for col in row:
        num_rows = col

for i in range(num_rows):
    id = i + 1
    org_id, country_id = unique_combo()

    query = f'UPDATE nbp_project.committee SET org_id = {org_id}, country_id = {country_id} WHERE id = {id}'
    cur.execute(query)
    inserted_pairs.add(f'{org_id}-{country_id}')
    print(cur.rowcount, inserted_pairs)

conn.commit()
cur.close()
conn.close()


"""
Logic:

keep track of the inserted combinations of org id and country id
go row by row, that is, for each id in the committee table
update the row with a new random combination of org id and committee id
but first check if there is already such a combination
if there is, try another random combination
try random combinations until u get a new unique one
insert the new unique combination
"""

"""
SQL - Run this locally (in DataGrip) to have the fixed data

create table nbp_project.temporary (
    id serial primary key,
    org_id integer,
    country_id integer,
    unique (org_id, country_id)
);

[import the file temporary-for-committee.csv]

insert into nbp_project.committee (org_id, country_id)
select org_id, country_id
from nbp_project.temporary;

"""