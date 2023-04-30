# Mark Bulmer - CIS 115 - 7-16-2021
# Programming Exercise 8-7

# Counts characters and whitespace in file "text.txt"
def main():

    # Local variables

    num_upper = 0
    num_lower = 0
    num_space = 0
    num_digits = 0
    data = ''

    infile = open('text.txt', 'r')
    # Read in data from the file
    data = infile.read()

    # Step through each character in the file
    for character in data:

        if character.isupper():
            num_upper = num_upper + 1

        if character.islower():
            num_lower = num_lower + 1

        if character.isdigit():
            num_digits = num_digits + 1

        if character.isspace():
            num_space = num_space + 1

    # Close the file
    infile.close()

    # Display the totals.
    print('The number of uppercase letters in the file:', num_upper)
    print('The number of lowercase letters in the file:', num_lower)
    print('The number of digits in the file:', num_digits)
    print('The number of whitespace in the file:', num_space)

# main
main()