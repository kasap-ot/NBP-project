import random
import csv
import utils


# Get number of countries
num_countries = ...

with open('csv_files/countries.csv', 'r') as file:
    reader = csv.reader(file)
    rows = list(reader)
    num_countries = len(rows)
    print(num_countries)


# Get number of organizations
num_organizations = ...

with open('csv_files/organizations.csv', 'r') as file:
    reader = csv.reader(file)
    rows = list(reader)
    num_organizations = len(rows)
    print(num_organizations)


# Generate and write committee info to csv file
num_committees = 1000

with open('csv_files/committees.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    for i in range(num_committees):
        phone_number = utils.random_phone_number()
        email = utils.random_email()
        address = utils.random_address()
        country_id = random.randint(1, num_countries)
        organization_id = random.randint(1, num_organizations)

        writer.writerow([
            phone_number,
            email,
            address,
            country_id,
            organization_id,
        ])

    print('END')
