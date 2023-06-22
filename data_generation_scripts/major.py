import csv
import utils as u

num_majors = 50

with open('csv_files/majors.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for i in range(num_majors):
        major = u.random_syllable_sequence(3).capitalize() + ' ' + \
                u.random_syllable_sequence(3).capitalize()

        writer.writerow([major])

    print('END')
