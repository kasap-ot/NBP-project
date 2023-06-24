import random
import csv
import utils
from country import get_num_countries


# num_countries = get_num_countries()
# print(num_countries)

# num_end_users = 20_000

# with open('csv_files/end_users.csv', 'w', newline='') as file:
#     writer = csv.writer(file)

#     for i in range(num_end_users):
#         username = utils.random_syllable_sequence(random.randint(2, 5)) + str(i)
#         password = utils.random_alphanumeric_sequence(10, 10)
#         name = utils.random_name()
#         surname = utils.random_surname()
#         date_of_birth = utils.random_date('1995-01-01', '2005-12-31')
#         address = utils.random_address()
#         phone = utils.random_phone_number()
#         email = utils.random_email()
#         country_id = random.randint(1, num_countries)

#         writer.writerow([
#             username,
#             password,
#             name,
#             surname,
#             date_of_birth,
#             address,
#             phone,
#             email,
#             country_id,
#         ])

#     print('END')

# _____________________________________


with open('csv_files/end_users.csv', 'r') as file:
    r = csv.reader(file)
    usernames = set()

    for row in r:
        curr_username = row[0]
        usernames.add(curr_username)

    print(len(usernames))