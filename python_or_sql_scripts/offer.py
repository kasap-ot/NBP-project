import random
import csv
import utils
import time

start_time = time.time()

random.seed()

# NOTE: We should define this. For 1000 rows it takes about 1 sec.
total_rows = 10 

with open('csv_files/offer.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    for i in range(0, total_rows):
        requirements = utils.random_word_sequence(15)
        responsibilities = utils.random_word_sequence(15)
        benefits = utils.random_word_sequence(15)
        salary = random.randint(500, 5000)
        field = utils.random_word_sequence(3)
        start_date = utils.random_date(2023, 2024)
        duration_in_weeks = random.randint(4, 52)
        
        member_id = 1 # TODO: For now just a filler reference to the member-creator
        company_id = 1 # TODO: For now just a filler reference

        # NOTE: Uncomment when we decide to run this script
        writer.writerow([requirements,
                         responsibilities,
                         benefits,
                         salary,
                         field,
                         start_date,
                         duration_in_weeks,
                         member_id,
                         company_id
                        ])
        
        print([requirements,
                responsibilities,
                benefits,
                salary,
                field,
                start_date,
                duration_in_weeks,
                member_id,
                company_id])
        
end_time = time.time()

duration = end_time - start_time
print(duration)