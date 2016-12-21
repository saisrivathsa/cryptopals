
from findkeylen import findingkeylen
from finding_key import redirect
from challenge_5 import xor

if __name__ == "__main__":
    file = open('6.txt')
    string = (''.join([line.strip() for line in file])).decode('base64')
    keylen = findingkeylen(string)
    l =  len(string)
    key = ''
    for i in range( keylen ):
        key += redirect(string[i::keylen]) #sending i th element of every keylength sized block and finding the character of key for that position
    print "\nKey:"+key
    print "---------------------------------------------------------------------------------"
    print "DATA : \n"+xor(string,key)
    print "---------------------------------------------------------------------------------"
