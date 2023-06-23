import random as r
import csv
import utils as u

# Get the number of users and majors
num_users = u.num_rows_in_file('csv_files/end_users.csv')
num_majors = u.num_rows_in_file('csv_files/majors.csv')

# Helper array
study_levels = ['BACHELOR', 'MASTER', 'DOCTORAL']

# _______________________________________________________________

# Get the set of member ids. The student ids are the set difference
# between user ids and member ids
all_user_ids = set(range(1, num_users + 1))
member_ids = set()

with open('csv_files/members.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        member_id = int(row[0])
        member_ids.add(member_id)

student_ids = all_user_ids - member_ids
student_ids = list(student_ids)


# _______________________________________________________________


num_students = len(student_ids)

with open('csv_files/students.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for i in range(num_students):
        student_id = student_ids[i]
        study_level = r.choice(study_levels)
        gpa = round(r.uniform(6.00, 10.00), 2)
        
        if study_level == 'BACHELOR':
            credits = r.randint(0, 180)
        elif study_level == 'MASTER':
            credits = r.randint(180, 300)
        elif study_level == 'DOCTORAL':
            credits = r.randint(300, 420)
        else:
            credits = ''
        
        major_id = r.randint(1, num_majors)
        
        # NOTE: Hardcoded values, for the sake of time...
        educational_institute_id = r.randint(501, 5500)
        
        start_year = r.randint(2015, 2022)

        writer.writerow([
            student_id,
            study_level,
            gpa,
            credits,
            major_id,
            educational_institute_id,
            start_year,
        ])

    print('END')
