import csv
import random
import string
from datetime import date, timedelta, datetime

words = ['brown', 'staircase', 'unfortunate', 'final', 'flour',
         'period', 'file', 'groan', 'restoration', 'promote',
         'interrupt', 'jelly', 'uniform', 'lace', 'crystal',
         'product', 'sink', 'shine', 'square', 'exhibition',
         'show', 'superior', 'story', 'sheet', 'definition',
         'straighten', 'delay', 'path', 'denial', 'grace',
         'revenge', 'pavement', 'hope', 'car', 'opponent',
         'arrest', 'even', 'roar', 'capital', 'presidency',
         'rhythm', 'form', 'railcar', 'obligation', 'top',
         'passion', 'offensive', 'discourage', 'development', 'pack',
         ]

syllables = ['wuh', 'mi', 'vin', 'hi', 'um', 'ku', 'in', 'ha', 'weh', 'la',
             'ale', 'waz', 'ofu', 'sob', 'ho', 'zam', 'dom', 'fi', 'zuf', 'du',
             'vut', 'be', 'do', 'co', 'bi', 'gi', 'vu', 'nip', 'ado', 'ep',
             'mo', 'he', 'ca', 'tuj', 'laz', 'de', 'zoz', 'zoj', 'zih', 'di',
             'omo', 'zuw', 'ki', 'ke', 'pac', 'mom', 'wa', 'ri', 'cud', 'zi',
             'ife', 'er', 'ih', 'tif', 'pe', 'ote', 'ror', 'mis', 'ad', 'taz',
             'tos', 'na', 'bek', 'wib', 'mu', 'nug', 'lo', 'wot', 'der', 'ama',
             'dim', 'ko', 'wu', 'lid', 'we', 'ket', 'ni', 'keg', 'so', 'cot',
             'hic', 'gis', 'ufi', 'al', 'muf', 'ufu', 'jo', 'tet', 'umu', 'ji',
             'bop', 'evi', 'giz', 'vil', 'ro', 'bon', 'oza', 'emi', 'fis', 'pav',
             ]

surnames = ['Fowlie', 'Franklin', 'Gair', 'Gammie', 'Gifford', 'Gold', 'Greenan', 'Hanley',
            'Hare', 'Hetherington', 'Hind', 'Hoggan', 'Hollywood', 'Hoy', 'Islam', 'Izatt',
            'Kavanagh', 'Keay', 'Keddie', 'Kellock', 'Keogh', 'Laurenson', 'Laverty',
            'Leggat', 'Lynas', 'Macritchie', 'Mactaggart', 'Mains', 'Markey', 'Masterton',
            'Mcaleese', 'Mcallan', 'Mccauley', 'Mccreath', 'Mccrossan', 'Mcelroy',
            'Mcgeachy', 'Mcgilvray', 'Mcphillips', 'Mcveigh', 'Mudie', 'Nichols',
            'Nightingale', 'Norton', 'Ord', 'Paisley', 'Paris', 'Parkin', 'Pender',
            'Pentland', 'Power', 'Purcell', 'Pyper', 'Rahman', 'Renfrew', 'Rhodes', 'Riach',
            'Riches', 'Rolland', 'Rush', 'Ruthven', 'Senior', 'Seymour', 'Simmonds', 'Singer',
            'Smeaton', 'Stead', 'Stitt', 'Stocks', 'Storey', 'Tanner', 'Third', 'Timmons',
            'Toal', 'Usman', 'Valente', 'Wheatley', 'Whitaker', 'Whiting', 'Winning',
            'Winters', 'Afzal', 'Aziz', 'Bacon', 'Baines', 'Bett', 'Blakely', 'Bowers', 'Britton',
            'Brockie', 'Brydon', 'Cairnie', 'Carlton', 'Carrick', 'Carstairs', 'Cattanach',
            'Chadwick', 'Coats', 'Cochran', 'Conlan', 'Cree', 'Creighton', 'Crook', 'Deas',
            'Denham', 'Dennison', 'Donohoe', 'Drake', 'Duke', 'Durrand', 'Eaglesham', 'English',
            'Esslemont', 'Fearn', 'Ferries', 'Fitzgerald', 'Fortune', 'Frater', 'Gamble', 'Gaughan',
            'Gillen', 'Goodman', 'Granger', 'Harte', 'Haston', 'Hawthorn', 'He', 'Hennessy', 'Herkes',
            'Hillhouse', 'Howitt', 'Irons', 'Jeffery', 'Kelbie', 'Kent', 'Kiernan', 'Leadbetter',
            'Linklater', 'Lodge', 'Lovie', 'Loy', 'Lundie', 'Macneill', 'Mahoney', 'Maley', 'Mallon',
            'Maltman', 'Mcalister', 'Mccleary', 'Mccolgan', 'Mccrory', 'Mcgarva', 'Mcginness',
            'Mcgonigle', 'Mckain', 'Mcleary', 'Mcleman', 'Mcnicoll', 'Mcvie', 'Meehan', 'Mulgrew',
            'Noon', 'Notman', 'Pate', 'Patel', 'Pattie', 'Peck', 'Peddie', 'Plunkett', 'Proudfoot',
            'Purvis', 'Rigby', 'Robbins', 'Roe', 'Sadler', 'Sellar', 'Sheikh', 'Sherriff',
            'Sillars', 'Spowart', 'Stanners', 'Stirrat', 'Storrie', 'Suttie', 'Swanston',
            'Symon', 'Tariq', 'Terry', 'Tinney', 'Tran', 'Twaddle', 'Vaughan', 'Wallis', 'Warden',
            'Wardle', 'Ware', 'Wilkins', 'Wynn', 'Yeats', 'Younger']

names = ['Oliver', 'Noah', 'Henry', 'William', 'Theodore', 'Hudson', 'Jack', 'Charlie', 'Elijah',
         'Leo', 'Thomas', 'Archie', 'Harrison', 'Archer', 'Levi', 'Lucas', 'James', 'Luca',
         'George', 'Harry', 'Hunter', 'Mason', 'Oscar', 'Arlo', 'Arthur', 'Cooper', 'Harvey',
         'Liam', 'Lachlan', 'Ethan', 'Carter', 'Lincoln', 'Finn', 'Alexander', 'Benjamin',
         'Riley', 'Kai', 'Hugo', 'Xavier', 'Samuel', 'Max', 'Eli', 'Flynn', 'Joseph', 'Sebastian',
         'Patrick', 'Beau', 'Jackson', 'Isaac', 'Theo', 'Austin', 'Ezra', 'Jaxon', 'Jacob',
         'Edward', 'Parker', 'Jasper', 'Connor', 'Sonny', 'Spencer', 'Luka', 'Angus', 'Ryan',
         'Wyatt', 'Jordan', 'Charles', 'River', 'Louis', 'Joshua', 'Billy', 'Grayson', 'Hamish',
         'Ryder', 'Phoenix', 'Braxton', 'Lennox', 'Michael', 'Fletcher', 'Asher', 'Bodhi',
         'Daniel', 'Ashton', 'Nate', 'Caleb', 'Darcy', 'Koa', 'Luke', 'Miles', 'Ari', 'Louie',
         'Owen', 'Vincent', 'Maxwell', 'Huxley', 'Elias', 'Matthew', 'Jayden', 'Ezekiel', 'Blake',
         'Chase', 'Isla', 'Olivia', 'Charlotte', 'Willow', 'Mia', 'Ava', 'Grace', 'Amelia',
         'Matilda', 'Lily', 'Ivy', 'Harper', 'Ella', 'Sophie', 'Evie', 'Ruby', 'Evelyn',
         'Isabella', 'Frankie', 'Lucy', 'Chloe', 'Mila', 'Sophia', 'Georgia', 'Violet', 'Layla',
         'Ellie', 'Aria', 'Luna', 'Audrey', 'Scarlett', 'Zoe', 'Hazel', 'Elsie', 'Penelope',
         'Alice', 'Poppy', 'Sienna', 'Aurora', 'Freya', 'Florence', 'Isabelle', 'Hannah',
         'Abigail', 'MacKenzie', 'Daisy', 'Emily', 'Eleanor', 'Ayla', 'Maya', 'Emilia',
         'Savannah', 'Billie', 'Eloise', 'Sadie', 'Bonnie', 'Remi', 'Emma', 'Stella', 'Summer',
         'Harriet', 'Sofia', 'Addison', 'Peyton', 'Piper', 'Elizabeth', 'Lola', 'Phoebe',
         'Charlie', 'Millie', 'Imogen', 'Maddison', 'Harlow', 'Delilah', 'Olive', 'Bella',
         'Claire', 'Zara', 'Quinn', 'Hallie', 'Thea', 'Pippa', 'Jasmine', 'Adeline', 'Lyla',
         'Eva', 'Rosie', 'Lilly', 'Indiana', 'Octavia', 'Maeve', 'Eden', 'Gracie', 'Aaliyah',
         'Brooklyn', 'Heidi', 'Aubrey', 'Lillian', 'Maggie', 'Rose']


def random_alphabetic_sequence_with_random_length(min_length: int, max_length: int) -> str:
    N = random.randint(min_length, max_length)
    sequence = ""
    for i in range(0, N):
        sequence = sequence + random.choice(string.ascii_letters)
    return sequence


def random_alphanumeric_sequence(min_length: int, max_length: int) -> str:
    N = random.randint(min_length, max_length)
    sequence = ""
    for i in range(0, N):
        sequence = sequence + random.choice(string.ascii_letters + string.digits)
    return sequence


def random_digits_sequence(length: int) -> str:
    sequence = ""
    for i in range(length):
        sequence = sequence + str(random.randint(0, 9))
    return sequence


def random_word_sequence(length: int) -> str:
    random_words = random.sample(words, length)
    separator = ' '
    sequence = separator.join(random_words)

    return sequence


def random_syllable_sequence(length: int) -> str:
    sequence = ""

    for i in range(length):
        random_syllable = random.choice(syllables)
        sequence += random_syllable

    return sequence


def random_name() -> str:
    return random.choice(names)


def random_surname() -> str:
    return random.choice(surnames)


def random_address() -> str:
    return  "c. "   + random_syllable_sequence(random.randint(2, 5)) + \
            " st. " + random_syllable_sequence(random.randint(2, 5)) + \
            " no. " + random_digits_sequence(3)


def random_phone_number() -> str:
    return random_digits_sequence(9)


def random_email() -> str:
    return random_syllable_sequence(random.randint(3, 5)) + "@"  +  \
           random_syllable_sequence(random.randint(3, 5)) + "."  +  \
           random_syllable_sequence(1)


def random_gpa() -> float:
    return round(random.uniform(6, 10), 2)


def random_date(start: str, end: str) -> str:
    format = '%Y-%m-%d'
    
    start_date = datetime.strptime(start, format)
    end_date = datetime.strptime(end, format)
    
    delta_date = end_date - start_date
    delta_days = delta_date.days
    random_days = random.randint(0, delta_days)
    
    random_date = start_date + timedelta(days=random_days)
    
    return random_date.date().isoformat()


def random_percent() -> str:
    return format(random.uniform(0, 100), '.2f')


def random_year() -> int:
    current_year = datetime.now().year
    return random.randint(2010, current_year)


def random_employee_num() -> int:
    employee_nums = [
        5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 
        100, 120, 140, 160, 180, 200, 250, 300, 
        350, 400, 450, 500, 600, 700, 800, 900, 1000,
    ]
    return random.choice(employee_nums)


def num_rows_in_file(file_path: str) -> int:
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        num_rows = len(rows)
        return num_rows
