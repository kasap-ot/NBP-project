import utils as u
import random as r
import csv

# _________________________________________________________

student_ids = []

with open('csv_files/students.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        curr_id = int(row[0])
        student_ids.append(curr_id)

# _________________________________________________________

num_languages = u.num_rows_in_file('csv_files/languages.csv')
language_levels = [ 'A1', 'A2', 'B1', 'B2', 'C1', 'C2' ]

# _________________________________________________________

num_knows_language = 20_000

with open('csv_files/knows_languages.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for i in range(num_knows_language):
        level = r.choice(language_levels)
        student_id = r.choice(student_ids)
        language_id = r.randint(1, num_languages)

        writer.writerow([
            level,
            student_id,
            language_id,
        ])

    print('END')
