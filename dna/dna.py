import csv
import sys


def main():

    # Check for command-line usage
    if len(sys.argv) != 3:
        print('Bruh.')
        sys.exit(1)

    # Read database file into a variable
    database = []
    with open(sys.argv[1], 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            database.append(row)

    # Read DNA sequence file into a variable
    with open(sys.argv[2], 'r') as file:
        dna = file.read()

    # TODO: Find longest match of each STR in DNA sequence
    strs = []
    temp = database[0]
    for pie in temp:
        strs.append(pie)

    dnaprofile = {}
    for i in range(1, len(strs), 1):
        dnaprofile[strs[i]] = longest_match(dna, strs[i])

    # Check database for matching profiles
    check = 0
    found = 0
    for j in range(len(database)):
        for pie in dnaprofile:
            if dnaprofile[pie] == int(database[j][pie]):
                check += 1
        if check == len(dnaprofile):
            name = database[j]['name']
            found = 1
            break
        else:
            check = 0

    # Print outcome
    if found == 1:
        print(name)
    else:
        print('No Match')

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
