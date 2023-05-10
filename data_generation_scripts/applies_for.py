import csv
import random
import utils
import time

start_time = time.time()

status_types = ['applied', 'accepted', 'rejected', 'ongoing', 'completed']

# _________________________________________________________________

# For assigning the foreign key of the row in the applies_for table

student_ids = list()

with open('csv_files/student.csv', 'r') as student_file:
    reader = csv.reader(student_file)
    for row in reader:
        for item in row:
            student_ids.append(int(item))

# _________________________________________________________________

number_of_offers = 1_003_600
applications_per_offer = 10
total_rows = number_of_offers * applications_per_offer

with open('csv_files/applies_for.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for i in range(0, total_rows):
        student_id = random.choice(student_ids)
        offer_id = random.randint(1, number_of_offers)
        acceptance_status = random.choice(status_types)
        
        # NOTE: The date of submission must be before the starting date of the internship
        date_of_submission = utils.random_date('2023-01-01', '2023-12-31')

        new_row = [
            student_id,
            offer_id,
            acceptance_status,
            date_of_submission,
        ]

        writer.writerow(new_row)
        # print(i, ' - ', new_row)

end_time = time.time()

duration = end_time - start_time
print(duration)
