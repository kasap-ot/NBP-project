import random
import csv
import utils
import time


start_time = time.time()

member_ids = []

with open('csv_files/members.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        curr_id = int(row[0])
        member_ids.append(curr_id)

num_companies = utils.num_rows_in_file('csv_files/companies.csv')

# ______________________________________________________________________

salaries = [
    500, 600, 700, 800, 900, 
    1000, 1200, 1500, 1800, 2000, 
    2200, 2500, 2800, 3000, 3200, 
    3500, 3800, 4000, 4200, 4500, 
    4800, 5000,
]

# ______________________________________________________________________


num_offers = 2_000_000

with open('csv_files/offers.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for i in range(num_offers):
        requirements = utils.random_word_sequence(3).capitalize()
        responsibilities = utils.random_word_sequence(3).capitalize()
        benefits = utils.random_word_sequence(3).capitalize()
        salary = random.choice(salaries)
        field = utils.random_word_sequence(2).capitalize()
        start_date = utils.random_date('2023-07-01', '2024-07-01')
        duration_in_weeks = random.randint(4, 52) # From 1 month to 1 year
        member_id = random.choice(member_ids)
        company_id = random.randint(1, num_companies)

        # TODO: Need to add this in the big csv file!
        is_active = 'true' if random.randint(0, 1) else 'false'

        writer.writerow([
            requirements,
            responsibilities,
            benefits,
            salary,
            field,
            start_date,
            duration_in_weeks,
            member_id,
            company_id,
            is_active,
        ])

# ______________________________________________________________________

end_time = time.time()
print(end_time - start_time)
