import csv
import random
import utils
import time

start_time = time.time()

status_types = ['applied', 'accepted', 'rejected', 'ongoing', 'completed']

total_rows = 10_000

with open('csv_files/applies_for.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for i in range(0, total_rows):
        acceptance_status = status_types[random.randint(0, len(status_types)-1)]
        
        #TODO: Find a way to assure that the date of application will be before the start-date of the offer
        date_of_submission = utils.random_date(2023, 2024)
        
        # TODO: Change to be a random student id
        student_id = 1

        # TODO: Change to be a random offer id
        offer_id = 1

        new_row = [
            acceptance_status,
            date_of_submission,
            student_id,
            offer_id,
        ]

        # writer.writerow(new_row)

        print(new_row)

end_time = time.time()

duration = end_time - start_time
print(duration)

# NOTE: Approximately 4 seconds for 10,000 rows
# This table should theoretically have the most rows - this is the point of the application