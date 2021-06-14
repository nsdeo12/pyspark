import re
import rsa
import sys
publicKey, privateKey = rsa.newkeys(512)

print(publicKey,file=open('publicKey.pub','wt'))
print(privateKey,file=open('privateKey.prv','wt'))
check = True
while check:
    referenceId=input('Please enter your 12 digit reference id ')
    if not len(referenceId)==12:
        print('Reference id should contain 12 digits')
        continue
    elif not re.search('[0-9]',referenceId):
        print('Reference id should contain at least one digit')
        continue
    elif not re.search('[a-zA-Z]',referenceId):
        print('Reference id should contain at least one alphabet')
        continue
    elif not re.search('[@#]',referenceId):
        print('Reference id should contain @ or #')
        continue
    else:
        encodedRefId=rsa.encrypt(referenceId.encode(),publicKey)
        print('Reference id:\n',encodedRefId)
        check = True
        break
    
