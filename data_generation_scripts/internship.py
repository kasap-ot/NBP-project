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

with open('csv_files/applies_for.csv', 'r') as applications_file:
    reader = csv.reader(applications_file)
    for row in reader:
        status = row[2]
        
        if status != 'completed':
            continue
        
        student_id = row[0]
        offer_id = row[1]

        completed_offers.append(
            {
                'student_id': int(student_id),
                'offer_id': int(offer_id),
            }
        )

# ______________________________________________________________

total_rows = len(completed_offers)

with open('csv_files/internship.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for i in range(0, total_rows):
        grade_work = random.randint(1, 10)
        grade_accommodation = random.randint(1, 10)
        grade_student = random.randint(1, 10)
        comment_student = 'none' # utils.random_word_sequence(3)
        comment_company = 'none' # utils.random_word_sequence(3)
        duration_in_weeks = random.randint(4, 52)
        salary = random.randint(500, 5000)
        bonus_pay = random.randint(100, 1000)
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
        # print(i, new_row)

end_time = time.time()
duration = end_time - start_time
print(duration)
