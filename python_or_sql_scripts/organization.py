import random
import pandas as pd
import csv
import python_or_sql_scripts.utils as utils




if __name__ == '__main__':
    random.seed()
    total_countries = pd.read_csv('../csv_files/country.csv', header=None).shape[0]

    with open('../csv_files/organization.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        total_organizations= 5
        #за секоја организација се избира country_id по случаен избор.
        #Moже да се случи две или повеќе организации да имаат резиденција во иста држава.
        org_country_ids = [ random.randint(1,total_countries) for i in range(total_organizations)]
        for country_id in org_country_ids:
            name = "Organization " + utils.random_syllable_sequence(5)
            phone_number = utils.random_phone_number()
            email_address = utils.random_email()
            address = utils.random_address()
            writer.writerow([name,phone_number,email_address,address,country_id])
