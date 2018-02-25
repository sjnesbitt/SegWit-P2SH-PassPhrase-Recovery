import itertools
import os
import binascii
import random
import mnemonic    
import sys

def main_validate(seed_input,valid,seed_input_orig):
     """Checks for a valid bip39 seed from the given list of words."""
     from itertools import permutations
#     print("Inside main_validate :", seed_input)
     m = mnemonic.Mnemonic('english')
     test = True
     subset = []
     for subset in permutations(seed_input, len(seed_input)):
#	    print (' '.join(subset))
#	    print (len(subset), len(seed_input))
            if len(subset) == len(seed_input):
                if m.check(' '.join(subset)):
                    if subset != seed_input:
                        result = ' '.join(subset)
#			print (subset[0], seed_input_orig[0], subset[-1], seed_input_orig[-1])
			if ((subset[0] == seed_input_orig[0]) and (subset[-1]== seed_input_orig[-1])):
# this conditional is because I know my original passphrase started with and end with the right word thus
# the correct crc.   I do not want to evaluate the other possiblilities to discover my correct passphrase
				print (result)
			valid = True
                    else:
                        if subset == seed_input:
				test = False
				valid = False
			print  "There was a problem with the words you gave, maybe they are not on the bip39 word list or the number of words does not work."
                    break  # found a valid one, stop looking.
     return seed_input

def mix_words(seed_input):
        """Shuffles the words in the entry field."""
#	print("Inside mixwords ", seed_input)
        shuffled = random.sample(seed_input, len(seed_input))
#        print(shuffled)
	return shuffled		
line_input = []
seed_input = []
shuffled  = []
valid = True
x = 0
for line in sys.stdin:
     seed_input  = line.split()
     seed_input_orig = seed_input
while (valid):
	try:
		main_validate (seed_input, valid, seed_input_orig)
	except (KeyboardInterrupt, SystemExit):
		raise
	except:
		print "Stopping at your request"
	if valid:
		seed_input = mix_words(seed_input)
	else:
		SystemExit  # found all permutations and back to origninal
