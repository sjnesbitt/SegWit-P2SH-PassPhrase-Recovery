#!/bin/bash
cat input_passphrases | ruby GetMnemonicPhrases.rb 
cp Possible_Valid_Info* ./segwit-p2sh
cd ./segwit-p2sh
python3 ./generate_keystore_w_correct_address.py
