#!/usr/bin/env python3

# Created By: Tamer Zreg
# Date: Dec. 07, 2022
# This program generates 10 random numbers and adds them to a list,
# then it calculates the sum of those numbers and displays the average.


# Imports Module for Random.
import random

# Function definition.
def average_Calculator():

    # Initializes all the variables to 0
    sum = 0
    counter = 0
    counter2 = 0
    # Initializes random_num_list to a list.
    random_num_list = []

    # Loop for generating and displaying random number.
    for counter in range(0, 10):
        random_num = random.randint(0, 100)
        # Adds the random number to the list.
        random_num_list.append(random_num)
        # Displays the random number.
        print(f"Added {random_num} to number {counter} in list")
    # Loop for calculating the sum of the numbers.
    for counter2 in range(0, 10):
        # Calculates sum.
        sum = sum + random_num_list[counter2]
    # Calculates average.
    average = sum / 10
    # Displays Average.
    print(f"Your Average is {average}")


# Calls function.
def main():
    average_Calculator()


if __name__ == "__main__":
    main()
