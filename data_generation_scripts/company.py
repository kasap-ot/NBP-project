import random
import csv
import utils


# Get the number of countries
num_countries = ...

with open('csv_files/countries.csv', 'r') as file:
    reader = csv.reader(file)
    rows = list(reader)
    num_countries = len(rows)
    print(num_countries)


num_companies = 10_000

with open('csv_files/companies.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for i in range(num_companies):
        name = utils.random_syllable_sequence(3).capitalize()
        phone = utils.random_phone_number()
        email = utils.random_email()
        address = utils.random_address()
        country_id = random.randint(1, num_countries)
        num_employees = utils.random_employee_num()

        writer.writerow([
            name,
            phone,
            email,
            address,
            country_id,
            num_employees,
        ])
        
    print('END')