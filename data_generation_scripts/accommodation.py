import csv
import random
import utils
import time

start_time = time.time()

random.seed()

total_rows = 10_000

accommodation_types = ['dormitory', 'apartment-shared', 'apartment-individual', 'house']

with open('csv_files/accommodation.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for i in range(0, total_rows):
        phone_number = utils.random_phone_number()
        email = utils.random_email()
        address = utils.random_address()
        country_id = random.randint(1, 193) # There are 193 rows in country.csv
        start_date = utils.random_date('2023-01-01', '2024-12-31')
        end_date = utils.random_date(start_date, '2024-12-31')
        type = accommodation_types[random.randint(0, len(accommodation_types)-1)]
        description = utils.random_word_sequence(15)
        offer_id = random.randint(1, 10_000) # TODO: Change if we add more offers

        new_row = [
            phone_number,
            email,
            address,
            country_id,
            start_date,
            end_date,
            type,
            description,
            offer_id,
        ]
    
        writer.writerow(new_row)

        print(new_row)

end_time = time.time()

duration = end_time - start_time
print(duration)

# NOTE: Approximately 7 seconds for 10,000 rows ()