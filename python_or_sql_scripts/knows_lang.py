#knows_lang
import random
import pandas as pd
import csv

if __name__ == '__main__':
    random.seed()

    students_dataframe = pd.read_csv('../../NBP-project dok/csv_files/student.csv')
    student_ids = students_dataframe.iloc[:, 0].values
    # student_id = random.choice(student_ids)

    languages = pd.read_csv('../../NBP-project dok/csv_files/language.csv', header=None).shape[0]

    total_rows = 3000
    with open('../../NBP-project dok/csv_files/knows_language.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for i in range(0,total_rows):

            values = ["A1,A2,B1,B2,C1,C2"]
            level = random.choice(values)

            student_id = random.choice(student_ids)

            lang_id = str(random.randint(1,languages))

            writer.writerow([level,student_id,lang_id])