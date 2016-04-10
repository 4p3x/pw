##########################################
# encrypt password with passlib / sha256 #
# grob / 09042016                        #
##########################################

import getpass
from passlib.hash import sha256_crypt

#create hash
print("encrypt your pass with salted sha256")
pw_input = getpass.getpass("enter pass: ")

hash = sha256_crypt.encrypt(pw_input, rounds=200000, salt_size=16)

print("this is your encrypted pass: ")
print hash

hash = ""


#verify hash
##pw = getpass.getpass("enter pw: ")
##if sha256_crypt.verify(pw, hash):
##    print("correct.")
##else:
##    print("wrong.")
##
##
##print("done. bye.")

