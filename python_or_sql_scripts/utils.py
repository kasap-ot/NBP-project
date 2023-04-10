import random

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