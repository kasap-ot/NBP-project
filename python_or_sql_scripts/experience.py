#experience
import random
import pandas as pd
import csv
import utils
from datetime import date

if __name__ == '__main__':
    random.seed()

    students_dataframe = pd.read_csv('../../NBP-project dok/csv_files/student.csv')
    student_ids = students_dataframe.iloc[:, 0].values
    # student_id = random.choice(student_ids)

    total = 7000
    with open('../../NBP-project dok/csv_files/experience.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for i in range(0,total):
            values = ["employee", "internship"]
            type_of_job = random.choice(values)

            description = utils.random_alphabetic_sequence_with_random_length(20,30)

            start_date = utils.random_date("2016-1-1", "2023-3-31")

            duration_in_weeks = random.randint(1, 105)

            student_id = random.choice(student_ids)

            writer.writerow([type_of_job,description,start_date,duration_in_weeks,student_id])