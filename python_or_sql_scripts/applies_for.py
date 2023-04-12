import csv

total_rows = 10

with open('csv_files/applies_for.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for i in range(0, total_rows):
        acceptance_status = ...
        date_of_submission = ...
        student_id = ...
        offer_id = ...

        new_row = [
            acceptance_status,
            date_of_submission,
            student_id,
            offer_id,
        ]

        writer.writerow(new_row)

        print(new_row)