"""
    written by Srinivas Avireddy
    Date : 11/26/2013
    This program
    Checks if the string entered by the user is a palindrome.
"""

def isPalindrome(input):
    """ Checks if the string entered by the user is a palindrome """
    reverse = input[::-1]
    if input == reverse:
        return True
    else:
        return False

def main():

    input = raw_input('Enter number / string to check if it is a palindrome: ')
    if isPalindrome(input):
        print "%s is a palindrome" % (input)
    else:
        print "%s is not a palindrome" % (input)

if __name__=="__main__":
    main()
