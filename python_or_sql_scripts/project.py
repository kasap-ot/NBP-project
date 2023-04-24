#project
import random
import pandas as pd
import csv
import utils

if __name__ == '__main__':
    random.seed()

    students_dataframe = pd.read_csv('../../NBP-project dok/csv_files/student.csv')
    student_ids = students_dataframe.iloc[:, 0].values
    # student_id = random.choice(student_ids)

    total = 5000
    with open('../../NBP-project dok/csv_files/project.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for i in range(0,total):

            name = "Project: " + utils.random_alphabetic_sequence_with_random_length(10,50-len("Certificate "))

            description = utils.random_alphabetic_sequence_with_random_length(20,30)

            completeness = utils.random_percent()

            student_id = random.choice(student_ids)

            writer.writerow([name,description,completeness,student_id])