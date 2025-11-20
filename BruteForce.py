import sys
import itertools
import string
from BitVector import * 

#Produces all possible ascii letters and digits within the possible keyspace
allChars = string.ascii_letters + string.digits

#This will createa all possible iterations of all potential keys in the keyspace giving the previous defined characters of the keyspace
#It does this by taking an empty space and joining it with a variable p, for however many p's are in the product of all possible
#character pairs
possibleChars = [''.join(p) for p in itertools.product(allChars, repeat=2)]

BLOCKSIZE = 16
numbytes = BLOCKSIZE // 8

if len(sys.argv) !=3:
    sys.exit('''Needs two command-line arguments, one for '''
             '''the encrypted file and the other for the '''
             '''decrypted output file''')

def main():
    #Main holds the function of just trying each possible combination of keys until it finds it, then will print out the key
    #that properly decrypts the given encrypted.txt file using the BitVector import

    solved = False
    while not solved:
        #Try a possible key

        #Attempt to decrypt text
        #If not decrypted into the original plaintext, not correct, try again

        break

    return





if __name__ == "__main__":
    main()