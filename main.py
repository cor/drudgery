import random
import time

from regex import findall
from statistics import mean
from pyfiglet import figlet_format

EXPERIMENT_COUNT = 200_000
GRAPH_WIDTH = 50


# Generate a sequence of 100 'H' (Heads) and 'T' (Tails) throws
# and return the amount of 6-long chains of the same value
def experiment_a():
    """The original"""
    flip_results = random.choices(('H', 'T'), k=100)
    streak_count = 0
    for i in range(len(flip_results) - 6):
        if ('T' not in flip_results[i:i + 6]) or ('H' not in flip_results[i:i + 6]):
            streak_count += 1
    return streak_count


def experiment_b():
    """The authentic original original."""
    flip_results = random.choices(('H', 'T'), k=100)
    streak_count = 0
    for i in range(len(flip_results) - 6):
        if (flip_results[i] == 'H' and 'T' not in flip_results[i:i + 6]) or (
                flip_results[i] == 'T' and 'H' not in flip_results[i:i + 6]):
            streak_count += 1
    return streak_count


def experiment_c():
    """We thought we were being smart here"""
    flip_results = "".join(random.choices(('H', 'T'), k=100))
    streak_count = 0
    for i in range(len(flip_results) - 6):
        if (flip_results[i:i + 6] == "T" * 6) or (
                flip_results[i:i + 6] == "H" * 6):
            streak_count += 1
    return streak_count


def experiment_d():
    """No string replication for extra speed. No strings attached."""
    flip_results = "".join(random.choices(('H', 'T'), k=100))
    streak_count = 0
    for i in range(len(flip_results) - 6):
        if (flip_results[i:i + 6] == "TTTTTT") or (
                flip_results[i:i + 6] == "HHHHHH"):
            streak_count += 1
    return streak_count


def experiment_e():
    """e."""
    flip_results = "".join(random.choices(('H', 'T'), k=100))
    streak_count = 0
    for i in range(len(flip_results) - 6):
        if (flip_results[i:i + 6] == flip_results[i] * 6):
            streak_count += 1
    return streak_count


def experiment_f():
    """Our old favourite"""
    flip_results = "".join(random.choices(('H', 'T'), k=100))
    streak_count = 0
    for i in range(len(flip_results) - 6):
        streak_count += (flip_results[i:i + 6] == flip_results[i] * 6)
    return streak_count


def experiment_g():
    """streak_count += (flip_results[i:i+6] in ('TTTTTT', 'HHHHHH'))"""
    flip_results = "".join(random.choices(('H', 'T'), k=100))
    streak_count = 0
    for i in range(len(flip_results) - 6):
        streak_count += (flip_results[i:i + 6] in ('TTTTTT', 'HHHHHH'))
    return streak_count

def experiment_g2():
    """streak_count += (flip_results[i:i+6] in ('TTTTTT', 'HHHHHH')) choice"""
    flip_results = "".join(random.choice(('H', 'T')) for i in range(100))
    streak_count = 0
    for i in range(len(flip_results) - 6):
        streak_count += (flip_results[i:i + 6] in ('TTTTTT', 'HHHHHH'))
    return streak_count


def experiment_h():
    """(flip_results[i:i+6] == "HHHHHH" ∨ flip_results[i:i+6] == "TTTTTT")"""
    flip_results = "".join(random.choices(('H', 'T'), k=100))
    streak_count = 0
    for i in range(len(flip_results) - 6):
        streak_count += (flip_results[i:i + 6] == "HHHHHH"
                         or flip_results[i:i + 6] == "TTTTTT")
    return streak_count


def experiment_i():
    """Same as h but we cache a var"""
    flip_results = "".join(random.choices(('H', 'T'), k=100))
    streak_count = 0
    for i in range(len(flip_results) - 6):
        temp = flip_results[i:i + 6]
        streak_count += (temp == "HHHHHH" or temp == "TTTTTT")
    return streak_count

def experiment_k():
    "Leon's test"
    flip_results = "".join(random.choice(('H', 'T')) for i in range(100))

    streaks_H = len(findall("HHHHHH", flip_results, overlapped=True))
    streaks_T = len(findall("TTTTTT", flip_results, overlapped=True))

    return streaks_H + streaks_T

def experiment_k2():
    "Leon's test choices"
    flip_results = "".join(random.choices(('H', 'T'), k=100))

    streaks_H = len(findall("HHHHHH", flip_results, overlapped=True))
    streaks_T = len(findall("TTTTTT", flip_results, overlapped=True))

    return streaks_H + streaks_T


def experiment_l():
    "Leon's test"
    flip_results = "".join(random.choice(('H', 'T')) for i in range(100))

    streaks = len(findall("HHHHHH|TTTTTT", flip_results, overlapped=True))

    return streaks


def experiment_l2():
    "Leon's test choices"
    flip_results = "".join(random.choices(('H', 'T'), k=100))

    streaks = len(findall("HHHHHH|TTTTTT", flip_results, overlapped=True))

    return streaks


def experiment_l3():
    "Art"
    flip_results = "".join(random.choices(('H', 'T'), k=100))

    return len(findall("HHHHHH|TTTTTT", flip_results, overlapped=True))


def experiment_l4():
    "One liner Art"
    return len(findall("HHHHHH|TTTTTT", "".join(random.choices(('H', 'T'), k=100)), overlapped=True))


def experiment_r():
    "Roos's algorithm"
    randomlist = []
    numberOfSequenceHeads = 0
    numberOfSequenceTails = 0
    numberOfStreaks = 0

    for experimentNumber in range(100):
        number = random.choice(['Heads','Tails'])
        randomlist.append(number)
    for i in range(len(randomlist)):
        if randomlist[i] == 'Heads':
            numberOfSequenceTails = 0
            numberOfSequenceHeads +=1
            if numberOfSequenceHeads ==6:
                numberOfStreaks +=1
        elif randomlist[i] == 'Tails':
            numberOfSequenceHeads = 0
            numberOfSequenceTails += 1
            if numberOfSequenceTails == 6:
                numberOfStreaks +=1
    return numberOfStreaks


def experiment_u_char():
    """Use bits in number to store coin-flip results (store as char)"""
    result = 0

    data = ['T'] * 100
    random_number = random.getrandbits(100)

    for current_character in range(0, 100):
        if random_number & (1 << current_character):
            data[current_character] = 'H'

    random_number = streak_length = 0
    last_character = ' '
    for current_character in data:
        if current_character == last_character:
            streak_length += 1
            if streak_length >= 6:
                random_number += 1
        else:
            streak_length = 1
            last_character = current_character

    result += random_number

    return result


def experiment_u_bits():
    """Use bits in number to store coin-flip results (use bits to process)"""
    number_of_samples = 100
    streak_length = 6

    data = random.getrandbits(100)

    result = 0
    length_of_current_streak = 0
    last_sample = None
    for sample_index in range(0, number_of_samples):
        sample = data & (1 << sample_index) == 0

        if sample != last_sample:
            length_of_current_streak = 1
            last_sample = sample
        else:
            length_of_current_streak += 1
            if length_of_current_streak >= streak_length:
                result += 1

    return result


def experiment_u_bits_mask():
    """Use bits in number to store coin-flip results and check with bit-mask (use bits to process)"""
    number_of_samples = 100
    streak_length = 6

    data = random.getrandbits(100)

    mask = 2 ** streak_length - 1

    result = 0
    for sample_index in range(0, number_of_samples - streak_length):
        current = data & mask

        if current == 0 or current == mask:
            result += 1

        data = data >> 1

    return result


# Test runner
def run_test(test_func):
    start_time = time.time()
    results = []
    for i in range(EXPERIMENT_COUNT):
        results.append(test_func())

    duration = time.time() - start_time
    print(f'Result: {mean(results)}')
    print(f'Time: \x1b[32m{duration}\x1b[0m')
    print()
    return duration


test_functions = [eval(lcl) for lcl in locals() if lcl.startswith("experiment_")]

results = {}
for test_func in test_functions:
    name = test_func.__name__
    print(f"Running \x1b[31m{name}\x1b[0m")
    print(test_func.__doc__)
    duration = run_test(test_func)

    results[name] = duration


print("\nThe Results:")

max_name_length = max(map(len, results.keys()))
max_value = max(results.values())
winner = sorted(results.items(), key=lambda item: item[1])[0][0]

for res in results:
    print(res.rjust(max_name_length, ' ')
        + ' | '
        + ('\x1b[32m' if res == winner else '\x1b[31m')
        + '═' * int(results[res] / max_value * GRAPH_WIDTH)
        + "\x1b[30m"
        + '═' * (GRAPH_WIDTH - int(results[res] / max_value * GRAPH_WIDTH))
        + (' \x1b[32m' if res == winner else ' \x1b[30m')
        + ("%.4fs" % round(results[res], 4))
        + "\x1b[0m")


print("\n\nAnd the absolute winner is...")
print(figlet_format(winner))
print(f"It seems that {eval(winner).__doc__} was the best approach after all")