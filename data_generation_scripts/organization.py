import random
import csv
import utils


num_organizations = 10

with open('csv_files/organizations.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    for i in range(num_organizations):
        name = utils.random_syllable_sequence(4).capitalize()
        phone_number = utils.random_phone_number()
        email = utils.random_email()
        address = utils.random_address()

        writer.writerow([
            name,
            phone_number,
            email,
            address,
        ])

    print('END')
