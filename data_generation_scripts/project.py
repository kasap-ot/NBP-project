import csv
import utils as u
import random as r


student_ids = list()
    
with open('csv_files/students.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        curr_id = int(row[0])
        student_ids.append(curr_id)

# __________________________________________________________________


completeness_levels = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

num_projects = 20_000

with open('csv_files/projects.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for i in range(num_projects):
        name = u.random_word_sequence(2).capitalize()
        description = u.random_word_sequence(5).capitalize()
        completeness = r.choice(completeness_levels)
        student_id = r.choice(student_ids)

        writer.writerow([
            name,
            description,
            completeness,
            student_id,
        ])

    print('END')