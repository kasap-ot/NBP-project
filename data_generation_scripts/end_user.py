import random
import pandas as pd
import csv
import python_or_sql_scripts.utils as utils




if __name__ == '__main__':
    random.seed()
    total_countries = pd.read_csv('../csv_files/country.csv', header=None).shape[0]
    end_user_per_country = 60
    with open('../csv_files/end_user.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for country_id in range(1, total_countries + 1):
            # За секоја држава внеси end_user_per_country крајни корисници
            for iter1 in range(end_user_per_country):
                username = utils.random_syllable_sequence(3) + utils.random_digits_sequence(4)
                password = utils.random_alphanumeric_sequence_with_random_length(8,15)
                name = utils.random_name()
                surname = utils.random_surname()
                date_of_birth = utils.random_date(1995,2001)
                address = utils.random_address()
                phone_number = utils.random_phone_number()
                email_address = utils.random_email()
                writer.writerow([username,password,name,surname,date_of_birth,address,phone_number,email_address,str(country_id)])
