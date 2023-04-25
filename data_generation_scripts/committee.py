import random
import pandas as pd
import csv
import python_or_sql_scripts.utils as utils



if __name__ == '__main__':
    random.seed()
    total_countries = pd.read_csv('../csv_files/country.csv', header=None).shape[0]

    organizations = pd.read_csv('../csv_files/organization.csv', header=None)
    total_organizations = organizations.shape[0]
    org_ids = [i for i in range(1, total_organizations + 1)]
    org_country_ids = organizations[4].values
    org_id_to_country_id = dict(zip(org_ids, org_country_ids))


    with open('../csv_files/committe.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        #за секоја организација се избира country_id по случаен избор.
        #Moже да се случи две или повеќе организации да имаат резиденција во иста држава.
        for org_id in range(1,total_organizations +1):
            for country_id in range(1,total_countries+1):
                total_committee = random.randint(1,10)
                for iter1 in range(0,total_committee):
                    phone_number = utils.random_phone_number()
                    email_address = utils.random_email()
                    address = utils.random_address()
                    writer.writerow([phone_number,email_address,address,str(country_id),str(org_id)])
