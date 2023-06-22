import csv
import utils
import random

num_committees = utils.num_rows_in_file('csv_files/committees.csv')
print(num_committees)

num_users = utils.num_rows_in_file('csv_files/end_users.csv')
print(num_users)

num_members = 10_000

# Get a subset of the user ids in a sorted order
all_user_ids = list(range(1, num_users + 1))
member_ids = random.sample(all_user_ids, num_members)
member_ids.sort()

with open('csv_files/members.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for i in member_ids:
        member_id = i
        committee_id = random.randint(1, num_committees)

        writer.writerow([
            member_id,
            committee_id,
        ])

    print('END')