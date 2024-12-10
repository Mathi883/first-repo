# These functions have been generated with the help of ChatGPT

def reduce_to_single_digit(num):
    # Reduce to single digit or master number
    while num > 9 and num not in [11, 22, 33]:
        num = sum(int(digit) for digit in str(num))
    return num

def calculate_life_path_number(dob):
    # Extract day, month, and year
    year = dob.year
    month = dob.month
    day = dob.day

    # Sum all digits of the date
    total_sum = sum(int(digit) for digit in f"{year}{month}{day}")

    # Reduce to a single digit or master number
    return reduce_to_single_digit(total_sum)

#This code was generated by ChatGPT
def calculate_destiny_number(name):
    # Mapping letters to numbers (A=1, B=2, ..., Z=26)
    letter_to_number = {
        letter: index for index, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ", start=1)
    }

    # Clean the input: remove spaces and make uppercase
    clean_name = name.replace(" ", "").upper()

    # Convert letters to numbers and sum them
    total = sum(letter_to_number.get(char, 0) for char in clean_name)

    # Reduce to a single digit or master number
    while total > 9 and total not in [11, 22, 33]:
        total = sum(int(digit) for digit in str(total))

    return total