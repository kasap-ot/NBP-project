import random

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


print(random_syllable_sequence(5))