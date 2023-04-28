import random
import csv
import time

start_time = time.time()

# _____________________________________________________________

student_ids = list()

with open('csv_files/student.csv', 'r') as student_file:
    reader = csv.reader(student_file)
    for row in reader:
        for item in row:
            student_ids.append(int(item))

# print(len(student_ids))

# _____________________________________________________________

training_ids = list()

with open('csv_files/training.csv', 'r') as training_file:
    reader = csv.reader(training_file)
    for row in reader:
        curr_id = int(row[0])
        training_ids.append(curr_id)

# print(len(training_ids))

# _____________________________________________________________


trainings_num = 1000
students_per_training = 10
total_rows = trainings_num * students_per_training

with open('csv_files/participates_in.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for i in range(0, total_rows):
        student_id = random.choice(student_ids)
        training_id = random.choice(training_ids)

        new_row = [
            student_id,
            training_id,
        ]

        writer.writerow(new_row)
        print(i, new_row)

end_time = time.time()
duration = end_time - start_time
print(duration)