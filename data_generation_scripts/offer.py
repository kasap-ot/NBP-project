import random
import csv
import utils
import time

start_time = time.time()

random.seed()

# ____________________________________________________________________

# First we need to read the ids of the members 
# so we can later insert them as foreign keys

member_ids = list()
members_file_path = 'csv_files/member.csv'

with open(members_file_path, 'r') as members_file:
    csv_reader = csv.reader(members_file)
    for row in csv_reader:
        for item in row:
            member_ids.append(int(item))

# ____________________________________________________________________

num_companies = 9650
offers_per_company = 10
total_rows = num_companies * offers_per_company

with open('csv_files/offer.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    for i in range(0, total_rows):
        requirements = utils.random_word_sequence(15)
        responsibilities = utils.random_word_sequence(15)
        benefits = utils.random_word_sequence(15)
        salary = random.randint(500, 5000)
        field = utils.random_word_sequence(3)
        start_date = utils.random_date('2024-01-01', '2024-12-31')
        duration_in_weeks = random.randint(4, 52)
        member_id = random.choice(member_ids)
        company_id = random.randint(1, num_companies) # There are 1000 rows in company.csv

        new_row = [requirements,
                    responsibilities,
                    benefits,
                    salary,
                    field,
                    start_date,
                    duration_in_weeks,
                    member_id,
                    company_id
                ]
        
        # writer.writerow(new_row)
        print(i, ' ---- ', new_row)
        
end_time = time.time()

duration = end_time - start_time
print(duration)