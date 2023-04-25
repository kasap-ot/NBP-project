
import csv, random, time

start_time = time.time()

total_rows = 10_000

with open('csv_files/won_prize.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for i in range(0, total_rows):

        student_id = random.randint(0, 10_000) # TODO: Good values?
        competition_id = random.randint(0, 1000) # TODO: Good values?
        place = random.randint(1, 3)

        new_row = [
            student_id,
            competition_id,
            place,
        ]

        # writer.writerow(new_row)

        print(new_row)

end_time = time.time()

duration = end_time - start_time
print(duration)