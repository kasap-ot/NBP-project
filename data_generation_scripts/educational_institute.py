import random as r
import csv
import utils as u

num_universities = 500
num_faculties = 5000

with open('csv_files/educational_institutes.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for i in range(num_universities):
        name = 'University of ' + u.random_syllable_sequence(4).capitalize()
        superior_id = ''

        writer.writerow([
            name,
            superior_id,
        ])

    for i in range(num_faculties):
        name = 'Faculty of ' + u.random_syllable_sequence(6).capitalize()
        superior_id = r.randint(1, num_universities)

        writer.writerow([
            name,
            superior_id,
        ])

    print('END')
