import csv
import random
import utils
import time
from datetime import datetime, timedelta

start_time = time.time()

# ______________________________________________________

def random_date_without_start(start_date, end_date):
    format = '%Y-%m-%d'
    
    start_date = datetime.strptime(start_date, format)
    end_date = datetime.strptime(end_date, format)
    
    delta = (end_date - start_date).days
    random_days = random.randint(1, delta)
    random_date = start_date + timedelta(days=random_days)
    
    return random_date.date().isoformat()

# ______________________________________________________

random.seed()

country_num = 193
offers_num = 1_003_600
accommodation_per_offer = 1
total_rows = offers_num * accommodation_per_offer

accommodation_types = ['dormitory', 'apartment-shared', 'apartment-individual', 'house']

with open('csv_files/accommodation.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for i in range(0, total_rows):
        phone_number = utils.random_phone_number()
        email = utils.random_email()
        address = utils.random_address()
        country_id = random.randint(1, country_num)
        
        start_date = utils.random_date('2024-01-01', '2024-12-31')
        end_date = random_date_without_start(start_date, '2024-12-31')
        
        type = random.choice(accommodation_types)
        description = utils.random_word_sequence(2)
        
        # The offers will be linked in reverse order
        offer_id = offers_num - i 

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
        # print(new_row)

end_time = time.time()

duration = end_time - start_time
print(duration)

# NOTE: Approximately 7 seconds for 10,000 rows ()