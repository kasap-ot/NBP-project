import random
import csv
import time

start_time = time.time()

total_rows = 10_000

with open('csv_files/participates_in.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for i in range(0, total_rows):
        student_id = random.randint(0, 10_000) # TODO: Check if values are good
        training_id = random.randint(0, 1000)  # TODO: Check if values are good

        new_row = [
            student_id,
            training_id,
        ]

        writer.writerow(new_row)

        print(new_row)

end_time = time.time()
duration = end_time - start_time
print(duration)