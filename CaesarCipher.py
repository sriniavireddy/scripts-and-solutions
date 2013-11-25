"""
   written by : Srinivas Avireddy
   Date       : 11/25/2013

   This python program is used to implement encryption and decryption of given text using
   Caesar cipher algorithm
"""

VALID_STRING = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(text,key):
    # used to encrypt a given input text
    # 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    
    encrypt_string = 'abcdefghijklmnopqrstuvwxyz' * 2
    output = ''
    for char in text:
        if char in VALID_STRING:
            index = encrypt_string.index(str(char))
            output += encrypt_string[index+key]
        else:
            output += char
    return output

def decrypt(text,key):
    # used to decrypt a given encrypted text
    # 'zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba'
    
    decrypt_string = 'zyxwvutsrqponmlkjihgfedcba' * 2
    output = ''
    for char in text:
        if char in VALID_STRING:
            index = decrypt_string.index(str(char))
            output += decrypt_string[index+key]
        else:
            output += char
    return output

if __name__ == '__main__':

    print """
    1. Press 1 to Encrypt text \n
    2. Press 2 to Decrypt text \n
    3. Press 3 to do both \n
    """
    choice = input('Enter a choice: ')
        
    if choice == 1:
        input_txt = raw_input('Enter the text to encrypt:')
        key       = input('Enter Key between 1 to 25 :')
        print "The encrypted text is : "
        print encrypt(input_txt, key)
        
    elif choice == 2:
        input_txt = raw_input('Enter the text to decrypt:')
        key       = input('Enter Key between 1 to 25 :')
        print "The decrypted text is : "
        print decrypt(input_txt, key)

    elif choice == 3:
        input_txt = raw_input('Enter the text:')
        key       = input('Enter Key between 1 to 25 :')
        
        print "The encrypted text is : "
        print encrypt(input_txt, key)
        
        print "The decrypted text is : "
        print decrypt(input_txt, key)
    else:
        print 'Invalid choice'

