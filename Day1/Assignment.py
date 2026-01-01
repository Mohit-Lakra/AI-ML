"""

Assignment: Write a script that simulates a "Data Loader" for a massive dataset.

Requirement 1: Create a function infinite_sequence() using a Generator (yield). It should start at 0 and yield num, num^2 forever (0, 0), (1, 1), (2, 4)...

Requirement 2: Create a function batch_processor(*args) that takes any number of tuples (from your generator) and prints them nicely. Use Type Hinting for the arguments.

Requirement 3: In your main loop, "fetch" the first 5 items from your infinite generator and pass them to the processor.

"""

from typing import Tuple

def infinite_sequence():
    num = 0
    while True:
        yield (num, num**2)
        num += 1

def batch_processor(*args: Tuple[int, int]) -> None:
    for item in args:
        print(f"Number: {item[0]}, Square: {item[1]}")


gen = infinite_sequence()
batch = []
for i in range(5):
    batch.append(next(gen))
batch_processor(*batch)
