#certificate
import random
import pandas as pd
import csv
import utils
from datetime import datetime, timedelta, date



if __name__ == '__main__':
    random.seed()

    students_dataframe = pd.read_csv('../../NBP-project dok/csv_files/student.csv')
    student_ids = students_dataframe.iloc[:, 0].values
    # student_id = random.choice(student_ids)

    total = 3000
    with open('../../NBP-project dok/csv_files/certificate.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for i in range(0,total):

            name = "Certificate: " + utils.random_alphabetic_sequence_with_random_length(5,30-len("Certificate "))

            description = utils.random_alphabetic_sequence_with_random_length(20,30)

            date_of_issue = utils.random_date("2018-1-1","2023-4-12")

            publisher = "Publisher: "+utils.random_alphabetic_sequence_with_random_length(10,30-len("Publisher: "))

            student_id = random.choice(student_ids)

            writer.writerow([name,description,date_of_issue,publisher,student_id])




