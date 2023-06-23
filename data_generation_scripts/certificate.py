import csv
import random as r
import utils as u

student_ids = list()
    
with open('csv_files/students.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        curr_id = int(row[0])
        student_ids.append(curr_id)

# ________________________________________________________

num_certificates = 20_000

with open('csv_files/certificates.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for i in range(num_certificates):
        name = u.random_word_sequence(2).capitalize()
        description = u.random_word_sequence(5).capitalize()
        date_of_issue = u.random_date('2015-01-01', '2023-05-31')
        publisher = u.random_syllable_sequence(4).capitalize()
        student_id = r.choice(student_ids)

        writer.writerow([
            name,
            description,
            date_of_issue,
            publisher,
            student_id,
        ])

    print('END')