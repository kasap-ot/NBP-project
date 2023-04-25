import utils
import random
import csv
import time

start_time = time.time()

total_rows = 10_000

with open('csv_files/internship.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for i in range(0, total_rows):
        grade_work = random.randint(0, 10)
        grade_accommodation = random.randint(0, 10)
        grade_student = random.randint(0, 10)
        comment_student = utils.random_word_sequence(15)
        comment_company = utils.random_word_sequence(15)
        duration_in_weeks = random.randint(4, 52)
        salary = random.randint(500, 5000)
        bonus_pay = random.randint(100, 1000)
        applies_for_student_id = 1 # TODO
        applies_for_offer_id = 1 # TODO

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

        # writer.writerow(new_row)

        print(new_row)

end_time = time.time()
duration = end_time - start_time
print(duration)

# NOTE: Approximately 7 seconds for 10,000 rows