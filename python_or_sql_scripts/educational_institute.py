import random
import pandas as pd
import csv
import python_or_sql_scripts.utils as utils



def generate_row_for_educational_institute(id,country_id,is_university=True,super_id=None):
    part_of_name=None
    superior_id = None
    if is_university == True:
        part_of_name ="University"
        superior_id = ""
    else:
        part_of_name = "Faculty"
        superior_id = str(super_id)

    name = part_of_name +" " +  utils.random_syllable_sequence(random.randint(5,10))
    phone_number = utils.random_phone_number()
    email_address = utils.random_email()
    address = utils.random_address()
    return [str(id),name,phone_number,email_address,address,superior_id,str(country_id)]


if __name__ == '__main__':
    random.seed()

    total_countries = pd.read_csv('../csv_files/country.csv', header=None).shape[0]
    universities_per_country = 3
    faculties_per_university = 10

    with open('../csv_files/educational_institute.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        global_id = 1
        for country_id in range(1,total_countries+1):
            # За секоја држава внеси universities_per_country универзитети
            for iter1 in range(universities_per_country):
                university_id= global_id
                global_id += 1
                row = generate_row_for_educational_institute(university_id,country_id,True,None)
                writer.writerow(row)
                #За секој универзитет внеси по faculties_per_university факултети
                for iter2 in range(faculties_per_university):
                    faculty_id = global_id
                    global_id += 1
                    row = generate_row_for_educational_institute(faculty_id,country_id,False,university_id)
                    writer.writerow(row)



