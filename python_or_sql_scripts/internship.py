import csv

total_rows = 10

with open('csv_files/internship.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for i in range(0, total_rows):
        grade_work = ...
        grade_accommodation = ...
        grade_student = ...
        comment_student = ...
        comment_company = ...
        duration_in_weeks = ...
        salary = ...
        bonus_pay = ...
        applies_for_student_id = ...
        applies_for_offer_id = ...

        new_row = [
            grade_work,
            grade_accommodation,
            grade_student,
            comment_student,
            comment_company,
            duration_in_weeks,
            salary,
            bonus_pay,
            applies_for_student_id,
            applies_for_offer_id,
        ]

        writer.writerow(new_row)

        print(new_row)