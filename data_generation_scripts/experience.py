import csv
import random as r
import utils as u

student_ids = []
    
with open('csv_files/students.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        curr_id = int(row[0])
        student_ids.append(curr_id)

# ________________________________________________________

num_experiences = 20_000

with open('csv_files/experiences.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for i in range(num_experiences):
        type_of_job = 'EMPLOYMENT' if r.randint(0, 1) == 1 else 'INTERNSHIP'
        description = u.random_word_sequence(5).capitalize()
        start_year = u.random_date('2015-01-01', '2022-01-01')
        duration_in_weeks = r.randint(4, 52) # from 1 month to 1 years experience
        student_id = r.choice(student_ids)

        writer.writerow([
            type_of_job,
            description,
            start_year,
            duration_in_weeks,
            student_id,
        ])

    print('END')