"""
    written by Srinivas Avireddy
    Date : 11/26/2013
    This program
    counts the number of vowels and count of each vowel.
"""

VOWELS = 'aeiou'

def computeVowelStats(input):
    """ computes the following:
    1. total count of vowels in the string --> stored in totalCount
    2. count of each vowel --> stored in vowelStatsMap
    """
    vowelStatsMap = { 'a':0, 'e':0, 'i':0, 'o':0, 'u':0 }
    totalCount = 0
    for char in input:
        if char in VOWELS:
            vowelStatsMap[char] += 1
            totalCount += 1
    return vowelStatsMap,totalCount

def main():
    input = raw_input('Enter the string : ')
    vowelStats, vowelCount = computeVowelStats(input)
    print "Total Vowel Count in the String = %d" %(vowelCount)
    print "------Vowel Stats--------"
    for vowel in VOWELS:
        print "count of %s = %d " % (vowel, vowelStats[vowel])

if __name__ == "__main__":
    main()
        
