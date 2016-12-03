from Crypto.Cipher import AES
def check(string):
    l =  len(string)/16
    for i in range (l) :
        for j in range (i+1,l) :
            if ( string[i*16:(i+1)*16] == string[j*16:(j+1)*16] ) : return True
    return False

file = open('8.txt')
for i in file :
    if check(i.strip().decode('hex')) : print i
