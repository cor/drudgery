import random
import time
import string

from pprint import pprint
from statistics import mean

# Generate a sequence of 100 'H' (Heads) and 'T' (Tails) throws
# and return the amount of 6-long chains of the same value
def experiment_a():
    flip_results = random.choices(('H', 'T'), k=100)
    streak_count = 0
    for i in range(len(flip_results)-6):
        if ('T' not in flip_results[i:i+6]) or ('H' not in flip_results[i:i+6]):
            streak_count += 1
    return streak_count


def experiment_b():
    flip_results = random.choices(('H', 'T'), k=100)
    streak_count = 0
    for i in range(len(flip_results)-6):
        if (flip_results[i] == 'H' and 'T' not in flip_results[i:i+6]) or (flip_results[i] == 'T' and 'H' not in flip_results[i:i+6]):
            streak_count += 1
    return streak_count


def experiment_c():
    flip_results = "".join(random.choices(('H', 'T'), k=100))
    streak_count = 0
    for i in range(len(flip_results)-6):
        if (flip_results[i:i+6] == "T"*6) or (flip_results[i:i+6] == "H"*6):
            streak_count += 1
    return streak_count

def experiment_d():
    flip_results = "".join(random.choices(('H', 'T'), k=100))
    streak_count = 0
    for i in range(len(flip_results)-6):
        if (flip_results[i:i+6] == "TTTTTT") or (flip_results[i:i+6] == "HHHHHH"):
            streak_count += 1
    return streak_count


def experiment_e():
    flip_results = "".join(random.choices(('H', 'T'), k=100))
    streak_count = 0
    for i in range(len(flip_results)-6):
        if (flip_results[i:i+6] == flip_results[i]*6):
            streak_count += 1
    return streak_count


def experiment_f():
    """Our old favourite"""
    flip_results = "".join(random.choices(('H', 'T'), k=100))
    streak_count = 0
    for i in range(len(flip_results)-6):
        streak_count += (flip_results[i:i+6] == flip_results[i]*6)
    return streak_count


def experiment_g():
    """streak_count += (flip_results[i:i+6] in ('TTTTTT', 'HHHHHH'))""" 
    flip_results = "".join(random.choices(('H', 'T'), k=100))
    streak_count = 0
    for i in range(len(flip_results)-6):
        streak_count += (flip_results[i:i+6] in ('TTTTTT', 'HHHHHH'))
    return streak_count


def experiment_h():
    """(flip_results[i:i+6] == "HHHHHH" or flip_results[i:i+6] == "FFFFFF")"""
    flip_results = "".join(random.choices(('H', 'T'), k=100))
    streak_count = 0
    for i in range(len(flip_results)-6):
        streak_count += (flip_results[i:i+6] == "HHHHHH" or flip_results[i:i+6] == "FFFFFF")
    return streak_count

def experiment_i():
    """Same as h but we cache a var"""
    flip_results = "".join(random.choices(('H', 'T'), k=100))
    streak_count = 0
    for i in range(len(flip_results)-6):
        temp = flip_results[i:i+6]
        streak_count += (temp == "HHHHHH" or temp == "FFFFFF")
    return streak_count


EXPERIMENT_COUNT = 20

"""
Cor predictions:
f is sneller dan e (geen if statement)
d is sneller dan c (geen string replicate operator)
b is sneller dan a (minder "in" checks)

D/C snelst, daarna F/E, daarna B/A

DCFEBA


Bart predictions:
b is sneller dan a (omdat eerder quit)
c is even snel als d (omdat iets met precompile?)
e is sneller dan f (je bespaart een type conversion, en += 1 is goedkoop)

C/D E F B A


A = 12.72
B 12.51

"""


def run_test(test_func):
    start_time = time.time()
    results = []
    for i in range(EXPERIMENT_COUNT):
        results.append(test_func())


    duration = time.time() - start_time
    print(f'Result: {mean(results)}')
    print(f'Time: {duration}')
    print()
    return duration



test_functions = [eval(f"experiment_{letter}") for letter in string.ascii_lowercase[:9]]

results = {}
for test_func in test_functions:
    name = test_func.__name__
    print(f"Running {name}")
    print(test_func.__doc__)
    duration = run_test(test_func)

    results[name] = duration

print("Results: ")
pprint(sorted(results.items(), key=lambda item: item[1]))