import random
import string
from datetime import date, timedelta

words = ['brown','staircase','unfortunate','final','flour',
         'period','file','groan','restoration','promote',
         'interrupt','jelly','uniform','lace','crystal',
         'product','sink','shine','square','exhibition',
         'show','superior','story','sheet','definition',
         'straighten','delay','path','denial','grace',
         'revenge','pavement','hope','car','opponent',
         'arrest','even','roar','capital','presidency',
         'rhythm','form','railcar','obligation','top',
         'passion','offensive','discourage','development','pack',
]

syllables = ['wuh','mi','vin','hi','um','ku','in','ha','weh','la',
             'ale','waz','ofu','sob','ho','zam','dom','fi','zuf','du',
             'vut','be','do','co','bi','gi','vu','nip','ado','ep',
             'mo','he','ca','tuj','laz','de','zoz','zoj','zih','di',
             'omo','zuw','ki','ke','pac','mom','wa','ri','cud','zi',
             'ife','er','ih','tif','pe','ote','ror','mis','ad','taz',
             'tos','na','bek','wib','mu','nug','lo','wot','der','ama',
             'dim','ko','wu','lid','we','ket','ni','keg','so','cot',
             'hic','gis','ufi','al','muf','ufu','jo','tet','umu','ji',
             'bop','evi','giz','vil','ro','bon','oza','emi','fis','pav',
]
surnames = ['Fowlie' ,'Franklin' ,'Gair' ,'Gammie' ,'Gifford' ,'Gold' ,'Greenan' ,'Hanley' ,
            'Hare' ,'Hetherington' ,'Hind' ,'Hoggan' ,'Hollywood' ,'Hoy' ,'Islam' ,'Izatt' ,
            'Kavanagh' ,'Keay' ,'Keddie' ,'Kellock' ,'Keogh' ,'Laurenson' ,'Laverty' ,
            'Leggat' ,'Lynas' ,'Macritchie' ,'Mactaggart' ,'Mains' ,'Markey' ,'Masterton' ,
            'Mcaleese' ,'Mcallan' ,'Mccauley' ,'Mccreath' ,'Mccrossan' ,'Mcelroy' ,
            'Mcgeachy' ,'Mcgilvray' ,'Mcphillips' ,'Mcveigh' ,'Mudie' ,'Nichols' ,
            'Nightingale' ,'Norton' ,'Ord' ,'Paisley' ,'Paris' ,'Parkin' ,'Pender' ,
            'Pentland' ,'Power' ,'Purcell' ,'Pyper' ,'Rahman' ,'Renfrew' ,'Rhodes' ,'Riach' ,
            'Riches' ,'Rolland' ,'Rush' ,'Ruthven' ,'Senior' ,'Seymour' ,'Simmonds' ,'Singer' ,
            'Smeaton' ,'Stead' ,'Stitt' ,'Stocks' ,'Storey' ,'Tanner' ,'Third' ,'Timmons' ,
            'Toal' ,'Usman' ,'Valente' ,'Wheatley' ,'Whitaker' ,'Whiting' ,'Winning' ,
            'Winters' ,'Afzal' ,'Aziz' ,'Bacon' ,'Baines' ,'Bett' ,'Blakely' ,'Bowers' ,'Britton' ,
            'Brockie' ,'Brydon' ,'Cairnie' ,'Carlton' ,'Carrick' ,'Carstairs' ,'Cattanach' ,
            'Chadwick' ,'Coats' ,'Cochran' ,'Conlan' ,'Cree' ,'Creighton' ,'Crook' ,'Deas' ,
            'Denham' ,'Dennison' ,'Donohoe' ,'Drake' ,'Duke' ,'Durrand' ,'Eaglesham' ,'English' ,
            'Esslemont' ,'Fearn' ,'Ferries' ,'Fitzgerald' ,'Fortune' ,'Frater' ,'Gamble' ,'Gaughan' ,
            'Gillen' ,'Goodman' ,'Granger' ,'Harte' ,'Haston' ,'Hawthorn' ,'He' ,'Hennessy' ,'Herkes' ,
            'Hillhouse' ,'Howitt' ,'Irons' ,'Jeffery' ,'Kelbie' ,'Kent' ,'Kiernan' ,'Leadbetter' ,
            'Linklater' ,'Lodge' ,'Lovie' ,'Loy' ,'Lundie' ,'Macneill' ,'Mahoney' ,'Maley' ,'Mallon' ,
            'Maltman' ,'Mcalister' ,'Mccleary' ,'Mccolgan' ,'Mccrory' ,'Mcgarva' ,'Mcginness' ,
            'Mcgonigle' ,'Mckain' ,'Mcleary' ,'Mcleman' ,'Mcnicoll' ,'Mcvie' ,'Meehan' ,'Mulgrew' ,
            'Noon' ,'Notman' ,'Pate' ,'Patel' ,'Pattie' ,'Peck' ,'Peddie' ,'Plunkett' ,'Proudfoot' ,
            'Purvis' ,'Rigby' ,'Robbins' ,'Roe' ,'Sadler' ,'Sellar' ,'Sheikh' ,'Sherriff' ,
            'Sillars' ,'Spowart' ,'Stanners' ,'Stirrat' ,'Storrie' ,'Suttie' ,'Swanston' ,
            'Symon' ,'Tariq' ,'Terry' ,'Tinney' ,'Tran' ,'Twaddle' ,'Vaughan' ,'Wallis' ,'Warden' ,
            'Wardle' ,'Ware' ,'Wilkins' ,'Wynn' ,'Yeats' ,'Younger']
names = ['Oliver' ,'Noah' ,'Henry' ,'William' ,'Theodore' ,'Hudson' ,'Jack' ,'Charlie' ,'Elijah' ,
         'Leo' ,'Thomas' ,'Archie' ,'Harrison' ,'Archer' ,'Levi' ,'Lucas' ,'James' ,'Luca' ,
         'George' ,'Harry' ,'Hunter' ,'Mason' ,'Oscar' ,'Arlo' ,'Arthur' ,'Cooper' ,'Harvey' ,
         'Liam' ,'Lachlan' ,'Ethan' ,'Carter' ,'Lincoln' ,'Finn' ,'Alexander' ,'Benjamin' ,
         'Riley' ,'Kai' ,'Hugo' ,'Xavier' ,'Samuel' ,'Max' ,'Eli' ,'Flynn' ,'Joseph' ,'Sebastian' ,
         'Patrick' ,'Beau' ,'Jackson' ,'Isaac' ,'Theo' ,'Austin' ,'Ezra' ,'Jaxon' ,'Jacob' ,
         'Edward' ,'Parker' ,'Jasper' ,'Connor' ,'Sonny' ,'Spencer' ,'Luka' ,'Angus' ,'Ryan' ,
         'Wyatt' ,'Jordan' ,'Charles' ,'River' ,'Louis' ,'Joshua' ,'Billy' ,'Grayson' ,'Hamish' ,
         'Ryder' ,'Phoenix' ,'Braxton' ,'Lennox' ,'Michael' ,'Fletcher' ,'Asher' ,'Bodhi' ,
         'Daniel' ,'Ashton' ,'Nate' ,'Caleb' ,'Darcy' ,'Koa' ,'Luke' ,'Miles' ,'Ari' ,'Louie' ,
         'Owen' ,'Vincent' ,'Maxwell' ,'Huxley' ,'Elias' ,'Matthew' ,'Jayden' ,'Ezekiel' ,'Blake' ,
         'Chase' ,'Isla' ,'Olivia' ,'Charlotte' ,'Willow' ,'Mia' ,'Ava' ,'Grace' ,'Amelia' ,
         'Matilda' ,'Lily' ,'Ivy' ,'Harper' ,'Ella' ,'Sophie' ,'Evie' ,'Ruby' ,'Evelyn' ,
         'Isabella' ,'Frankie' ,'Lucy' ,'Chloe' ,'Mila' ,'Sophia' ,'Georgia' ,'Violet' ,'Layla' ,
         'Ellie' ,'Aria' ,'Luna' ,'Audrey' ,'Scarlett' ,'Zoe' ,'Hazel' ,'Elsie' ,'Penelope' ,
         'Alice' ,'Poppy' ,'Sienna' ,'Aurora' ,'Freya' ,'Florence' ,'Isabelle' ,'Hannah' ,
         'Abigail' ,'MacKenzie' ,'Daisy' ,'Emily' ,'Eleanor' ,'Ayla' ,'Maya' ,'Emilia' ,
         'Savannah' ,'Billie' ,'Eloise' ,'Sadie' ,'Bonnie' ,'Remi' ,'Emma' ,'Stella' ,'Summer' ,
         'Harriet' ,'Sofia' ,'Addison' ,'Peyton' ,'Piper' ,'Elizabeth' ,'Lola' ,'Phoebe' ,
         'Charlie' ,'Millie' ,'Imogen' ,'Maddison' ,'Harlow' ,'Delilah' ,'Olive' ,'Bella' ,
         'Claire' ,'Zara' ,'Quinn' ,'Hallie' ,'Thea' ,'Pippa' ,'Jasmine' ,'Adeline' ,'Lyla' ,
         'Eva' ,'Rosie' ,'Lilly' ,'Indiana' ,'Octavia' ,'Maeve' ,'Eden' ,'Gracie' ,'Aaliyah' ,
         'Brooklyn' ,'Heidi' ,'Aubrey' ,'Lillian' ,'Maggie' ,'Rose']



def random_alphabetic_sequence_with_random_length(min_length, max_length):
    N = random.randint(min_length, max_length)
    sequence = ""
    for i in range(0,N):
        sequence= sequence + random.choice(string.ascii_letters)
    return sequence

def random_alphanumeric_sequence_with_random_length(min_length, max_length):
    N = random.randint(min_length, max_length)
    sequence = ""
    for i in range(0,N):
        sequence= sequence + random.choice(string.ascii_letters + string.digits)
    return sequence

def random_digits_sequence(length):
    sequence = ""
    for i in range(length):
        sequence = sequence + str(random.randint(0,9))
    return sequence

def random_word_sequence(length):
    sequence = ""
    words_count = len(words)
    
    for i in range(length):
        random_word = words[random.randint(0, words_count-1)]
        sequence += (' ' + random_word)
    
    return sequence

def random_syllable_sequence(length):
    sequence = ""
    syllables_count = len(syllables)

    for i in range(length):
        random_syllable = syllables[random.randint(0, syllables_count-1)]
        sequence += random_syllable

    return sequence


def random_name():
    return names[random.randint(0, len(names)-1)]

def random_surname():
    return surnames[random.randint(0, len(names)-1)]

def random_date(from_year,to_year):
    start_date = date(from_year, 1, 1)
    end_date = date(to_year, 12, 31)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)

    random_date = start_date + timedelta(days=random_number_of_days)
    return str(random_date)


def random_address():
    return "city: " + random_syllable_sequence(random.randint(5,10)) + \
              " street: " + random_syllable_sequence(random.randint(3,5)) + \
              " number: " + random_digits_sequence(4)


def random_phone_number():
    return random_digits_sequence(9)


def random_email():
    return random_syllable_sequence(random.randint(3,5)) + "@" + \
                   random_syllable_sequence(random.randint(3,5)) + "." + \
                   random_syllable_sequence(1)