import random


def main() -> None:
    """
    Main method which generates a user set amount of random passwords
    :return: None
    """
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~`!@#$%^&*()_-+={[}]|\:;<,>.?/1234567890'
    #User input for the number of passwords desired
    numPasswords = input("Please enter the number of passwords you would like: ")
    #loop to validate user input, making sure that it is a positive integer between 0-128. 128 was chosen arbitrarily
    while True:
        try:
            numPasswords = int(numPasswords)
            if int(numPasswords) <= 0 or int(numPasswords) > 128:
                numPasswords = input("Please enter a positive integer that is 128 or less: ")
            else:
                break
        except ValueError:
            numPasswords = input("Please enter a positive integer: ")
    #User input for the length of each password
    length = input("Please enter the desired length of these passwords: ")
    # loop to validate user input, making sure that it is a positive integer between 0-128. 128 was chosen arbitrarily
    while True:
        try:
            length = int(length)
            if int(length) <= 0 or int(length) > 128:
                length = input("Please enter a positive integer that is 128 or less: ")
            else:
                break
        except ValueError:
            length = input("Please enter a positive integer: ")
    #creates a list that the passwords will be added to
    passwords = []
    #nested for loop to generate a password character by character, adding each character to a string, then adding each string to a list
    for i in range(numPasswords):
        pword = ''
        for j in range(length):
            pword += random.choice(chars)
        passwords.append(pword)
    #for loop to print each password line by line
    for i in passwords:
        print(i)
    #signals that the program has ended
    print("End of program")


if __name__ == '__main__':
    main()
