import csv
import random as r
import utils as u
import time

start_time = time.time()

status_types = ['applied', 'accepted', 'rejected', 'ongoing', 'completed']

# _________________________________________________________________

student_ids = []

with open('csv_files/students.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        curr_id = int(row[0])
        student_ids.append(curr_id)

# _________________________________________________________________

offer_start_dates = []

with open('csv_files/offers.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        curr_start_date = row[5]
        offer_start_dates.append(curr_start_date)

# _________________________________________________________________


num_offers = len(offer_start_dates)
num_applications = 10_000_000

with open('csv_files/applications.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for i in range(num_applications):
        offer_id = r.randint(1, num_offers)
        
        # Need to shift to be correct
        curr_offer_start_date = offer_start_dates[offer_id - 1]

        # The date of application must be before the start date of the offer!
        date_of_application = u.random_date('2023-01-01', curr_offer_start_date)
        
        acceptance_status = r.choice(status_types)
        student_id = r.choice(student_ids)

        # Write columns in correct order
        writer.writerow([
            date_of_application,
            acceptance_status,
            student_id,
            offer_id,
        ])
    
    print('student ids: ', len(student_ids))
    print('offer start dates ids: ', len(offer_start_dates))
    print('offers: ', num_offers)
    print('applications: ', num_applications)
    
    print('END')

end_time = time.time()

print(end_time - start_time)
