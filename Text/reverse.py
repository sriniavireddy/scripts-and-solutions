"""
    written by Srinivas Avireddy
    Date : 11/26/2013
    This program
    computes the reverse of a string.
"""


def computeReverse(input):
    """
    computes reverse of a string
    """
    reverse = input[::-1]
    return reverse

def main():

    input = raw_input('Enter the string to reverse: ')
    reverse = computeReverse(input)
    print 'The reverse of %s is %s' %( input, reverse)
    
if __name__ == "__main__":
    main()
    
                      
