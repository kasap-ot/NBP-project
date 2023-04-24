#event
import random
import pandas as pd
import csv
import utils
from datetime import datetime, timedelta, date



if __name__ == '__main__':
    random.seed()

    countries = pd.read_csv('../../NBP-project dok/csv_files/country.csv', header=None).shape[0]
    committees = pd.read_csv('../../NBP-project dok/csv_files/committe.csv', header=None).shape[0]


    total_row = 1000
    with open('../../NBP-project dok/csv_files/event.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for i in range(0,total_row):

            name = "Event: " + utils.random_alphabetic_sequence_with_random_length(10, 50-len("Event: "))

            phone_number = utils.random_phone_number()

            email_address = utils.random_email()

            address = utils.random_address()

            start_date = utils.random_date("2020-1-1", "2023-4-12")

            end_date = (datetime.strptime(start_date, "%Y-%m-%d") + timedelta(days=7)).strftime("%Y-%m-%d")

            topic = utils.random_alphabetic_sequence_with_random_length(5,50)

            country_id = str(random.randint(1,countries))

            committee_id = str(random.randint(1, committees))


            writer.writerow([name,phone_number,email_address,address,start_date,end_date,topic,country_id,committee_id])