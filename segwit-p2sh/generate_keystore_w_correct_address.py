
import sys
from lib.keystore import from_bip39_seed
from lib.storage import WalletStorage
from lib.wallet import Standard_Wallet

def _create_standard_wallet(ks):
    gap_limit = 1  # make tests run faster
    store = WalletStorage('if_this_exists_mocking_failed_648151893')
    store.put('keystore', ks.dump())
    store.put('gap_limit', gap_limit)
    w = Standard_Wallet(store)
    w.synchronize()
    return w

def test_bip39_seed_bip49_p2sh_segwit(password,seed_input):
    # Change this to be YOUR seed phrase:
    #    seed_words = 'final round trust era topic march brain envelope spoon minimum bunker start'
    seed_words = seed_input
    # Change this to be the address you want to generate.
    # This example is generated with no password used (see calling statement in mainline
    # code below and the password = '');  If you set a password with you ledger passphrase then you
    # will need to go back to the orignator's code (see README.1st) Look at how he implemented
    # the varying password code.  I did not need it so I did not move it over.
    
    # Example:    address = '32ZGyqRWn9fPbLjztjYpxSMeACUgFtCD2c'

    address = '32FreULok9F42Uwd3hiCK3pWCne79nzN2Z' #Bip49
#    address = '1KdKaWcrriw4wGMwqJ4vVgbFP5eJ5sdV5L' #Bip44 

    # The BIP32/43 path below could be made a parameter:
    ks = from_bip39_seed(seed_words, password, "m/49'/0'/0'")
#    ks = from_bip39_seed(seed_words, password, "m/44'/0'/0'")
    w = _create_standard_wallet(ks)
    if (w.get_receiving_addresses()[0] == address):
        return True
    else:
        return False

		   

# Main

# Read valid  potential candidates and then create derivative addresses,
# then compare to txaddress(es)
password = ''
hit = False
list_lines = []
handle = open('Possible_Valid_Info_0', 'r')
if (handle != False) :
	for line in handle:
		list_lines = line.split(',') # list_lines contains 6 fields - the 6th is passphrase
		seed_input = list_lines[5]
#	print ('seed_input = ',seed_input)
		hit = test_bip39_seed_bip49_p2sh_segwit(password,seed_input)
		if hit == True:
			print ("Here is the correct Passphrase that was used to create a wallet that produced the specified Segwit-P2SH address")
			print (seed_input)
			break
	if hit == False:
		print ("None of these passphrases produced the BIP49 derivative address")
handle.close()
