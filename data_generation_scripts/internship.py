import utils
import random
import csv
import time
from typing import List, Dict

start_time = time.time()

# ______________________________________________________________

# A list of dictionaries containing the ids of the offers and students 
# corresponding to the completed offers i.e. the internships

completed_offers: List[Dict[str, int]] = list()

with open('csv_files/applications.csv', 'r') as file:
    reader = csv.reader(file)
    
    # Each row is: [date of application, status, student id, offer id]
    for row in reader:
        status = row[1]
        
        if status != '5':
            continue
        
        student_id = row[2]
        offer_id = row[3]

        completed_offers.append(
            {
                'student_id': int(student_id),
                'offer_id': int(offer_id),
            }
        )

completed_offers = random.sample(completed_offers, len(completed_offers))

print('completed offers: ', len(completed_offers))

salaries = [
    500, 600, 700, 800, 900, 
    1000, 1200, 1500, 1800, 2000, 
    2200, 2500, 2800, 3000, 3200, 
    3500, 3800, 4000, 4200, 4500, 
    4800, 5000,
]

bonuses = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

print('time for setup: ', time.time() - start_time)

# ______________________________________________________________

num_completed_offers = len(completed_offers)
print('num of completed offers: ', num_completed_offers)

with open('csv_files/internships.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for i in range(num_completed_offers):
        grade_work = random.randint(1, 10)
        grade_accommodation = random.randint(1, 10)
        grade_student = 0 # Filler value. Don't need this column
        comment_student = utils.random_word_sequence(3).capitalize()
        comment_company = 'none'
        duration_in_weeks = random.randint(4, 52)
        salary = random.choice(salaries)
        bonus_pay = random.choice(bonuses)
        applies_for_student_id = completed_offers[i]['student_id']
        applies_for_offer_id = completed_offers[i]['offer_id']

        new_row = [
            grade_work,
            grade_accommodation,
            grade_student,
            comment_student,
            comment_company,
            duration_in_weeks,
            salary,
            bonus_pay,
            applies_for_student_id,
            applies_for_offer_id,
        ]

        writer.writerow(new_row)


print('time to complete: ', time.time() - start_time)

