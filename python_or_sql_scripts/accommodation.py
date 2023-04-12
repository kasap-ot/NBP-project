import csv
import random

random.seed()

total_rows = 1

with open('csv_files/accommodation.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for i in range(0, total_rows):
        phone_number = ...
        email = ...
        address = ...
        country_id = ...
        start_date = ...
        end_date = ...
        type = ...
        description = ...
        offer_id = ...

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