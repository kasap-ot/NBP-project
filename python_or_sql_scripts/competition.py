#competition
import random
import pandas as pd
import csv
import utils
from datetime import datetime, timedelta, date



if __name__ == '__main__':
    random.seed()

    events = pd.read_csv('../../NBP-project dok/csv_files/event.csv', header=None).shape[0]

    total_row = 1000
    with open('../../NBP-project dok/csv_files/competition.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for i in range(0,total_row):

            id = str(random.randint(1, events))

            rules = "Rules: " + utils.random_alphabetic_sequence_with_random_length(10, 500-len("Rules: "))

            writer.writerow([id,rules])