#studies
import random
import pandas as pd
import csv
import utils

if __name__ == '__main__':
    random.seed()

    students_dataframe = pd.read_csv('../../NBP-project dok/csv_files/student.csv')
    student_ids = students_dataframe.iloc[:, 0].values
    #student_id = random.choice(student_ids)

    faculty_length = pd.read_csv('../../NBP-project dok/csv_files/educational_institute.csv', header=None).shape[0]

    total_studies = 10000

    with open('../../NBP-project dok/csv_files/studies.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for i in range(0, total_studies):

            faculty_id = str(random.randint(1, faculty_length))
            student_id = random.choice(student_ids)
            values = ["BACHELOR", "MASTER", "DOCTORAL"]
            study_level = random.choice(values)
            gpa = utils.random_gpa()
            start_year = utils.random_year()
            ects_credits = random.randint(100,240)

            writer.writerow([faculty_id,student_id,study_level,gpa,start_year,ects_credits])