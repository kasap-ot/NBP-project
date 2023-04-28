
import csv, random, time

start_time = time.time()

# ------------

student_ids = list()

with open('csv_files/student.csv', 'r') as student_file:
    reader = csv.reader(student_file)
    for row in reader:
        for item in row:
            student_ids.append(int(item))

print(len(student_ids))

# ------------

competition_ids = list()

with open('csv_files/competition.csv', 'r') as competition_file:
    reader = csv.reader(competition_file)
    for row in reader:
        curr_id = int(row[0])
        competition_ids.append(curr_id)

print(len(competition_ids))

# ------------

competition_num = len(competition_ids)
students_per_competition = 10
total_rows = competition_num * students_per_competition

with open('csv_files/won_prize.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for i in range(0, total_rows):

        student_id = random.choice(student_ids)
        competition_id = random.choice(competition_ids)
        place = random.randint(1, 3)

        new_row = [
            student_id,
            competition_id,
            place,
        ]

        writer.writerow(new_row)
        print(i, new_row)

end_time = time.time()

duration = end_time - start_time
print(duration)