# CS564Assignment6BruteForce
The goal is to implement a python script in which can brute force the encrypted text and decrypt it given the programs decryptForFun.py and encryptForFun.py were used to encrypt the message

# A little about the program
The script runs a little slow, so you will have to give it time to eventually find the key. Given any encrypted text file, you might need to increase the number of correct characters found between the potential decrypted text and the actual text if given. The program is not perfect, but it at least gets the decrypted text correct. The decrypted.txt file that is there within the other files was me testing if the program had correctly found a key using the brute force method by inputting the key into the DecryptForFun.py file, which was given for the assignment for reference.

# How to run
1. Have a python version installed, anything over version 3 already has library itertools and string installed
2. Run the newly implemented python script named BruteForce.py
    - You can do this by running the command line 'python BruteForce.py' or running it in any ide of your choosing
3. Wait a little while until the brute force method eventually finds the key used to decrypt the encrypted.txt given in the assignment writeup