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

member_ids_length = len(member_ids)

# ____________________________________________________________________

# NOTE: We should define this. For 1000 rows it takes about 1 sec.
total_rows = 100_000

with open('csv_files/offer.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    for i in range(0, total_rows):
        requirements = utils.random_word_sequence(15)
        responsibilities = utils.random_word_sequence(15)
        benefits = utils.random_word_sequence(15)
        salary = random.randint(500, 5000)
        field = utils.random_word_sequence(3)
        start_date = utils.random_date('2023-01-01', '2024-12-31')
        duration_in_weeks = random.randint(4, 52)
        
        member_id = member_ids[random.randint(0, member_ids_length-1)]
        company_id = random.randint(1, 1000) # There are 1000 rows in company.csv

        # NOTE: Uncomment when we decide to run this script
        writer.writerow([requirements,
                         responsibilities,
                         benefits,
                         salary,
                         field,
                         start_date,
                         duration_in_weeks,
                         member_id,
                         company_id
                        ])
        
        print([requirements,
                responsibilities,
                benefits,
                salary,
                field,
                start_date,
                duration_in_weeks,
                member_id,
                company_id])
        
end_time = time.time()

duration = end_time - start_time
print(duration)