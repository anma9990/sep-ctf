import hashlib
import sys
from time import sleep

with open('flag1.txt', 'r') as password_hash: 
    data = password_hash.readline().strip()

with open('common_passwords.txt','r') as file:
    counter = 0
    while 1:
        ###Fairly pointless counter
        sleep(0.001)
        counter+=1
        sys.stdout.write('\r')
        sys.stdout.write('Trying Password %d' % counter)
        sys.stdout.flush()
        ###
        password = file.readline().strip()
        hs = hashlib.sha256(password.encode('utf-8')).hexdigest()
        if (hs == data):
            print('\n' + password)
            break
