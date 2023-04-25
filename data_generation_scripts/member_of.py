#member_of
import random
import pandas as pd
import csv
import utils

if __name__ == '__main__':
    random.seed()

    members = pd.read_csv('../../NBP-project dok/csv_files/member.csv')
    members_ids = members.iloc[:, 0].values

    committees = pd.read_csv('../../NBP-project dok/csv_files/committe.csv', header=None).shape[0]


    total_members = 1000
    with open('../../NBP-project dok/csv_files/member_of.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for i in range(0, total_members):
            member_id = random.choice(members_ids)
            committee_id = str(random.randint(1, committees))

            writer.writerow([member_id, committee_id])

