from Crypto.Cipher import AES
from random import randint

def random_key_generator(l=16):
    key = ''.join([chr(randint(0,255)) for i in range(l)])
    return key


def pad(string, length = 16):
    l = length - (len (string) % length)
    return string + chr(l)*(l)

def unpad (data):
    l = ord( data [ len(data)-1 ] )
    flag = True
    for i in range(l):
        if data[-l] != data[-l+i]:
            flag = False
    if flag :
        return data[ : -l ]
    else :
        return "The data %s passed is not properly padded"%repr(data)
        
key = random_key_generator()

def ECB_encrypt(data, key=key):
    data = pad (data,16)
    mode = AES.new(key,AES.MODE_ECB)
    return mode.encrypt(data)

def ECB_decrypt(data,key=key):
    mode=AES.new(key,AES.MODE_ECB)
    return unpad(mode.decrypt(data))

def parse(data):
    data = data.split('&')
    data = [x.split('=') for x in data]
    return {x:y for x,y in data }

def profile_for(data,role='user'):
    if '=' in data:
        print "Illegal arguements passed "
    elif '&' in data :
        print "Illegal arguements passed "

    data = data.replace('=','').replace('&','')
    return "email=" + data + "&uid=10&role=" + role


if __name__ == "__main__" :
    #NORMAL
    print ECB_decrypt(ECB_encrypt(profile_for('srivathsaeric@gmail.com')))

    #HACK ATTEMPT
    print ECB_decrypt(ECB_encrypt(profile_for('srivathsaeric@gmail.com=')))

    #ADMIN
    print ECB_decrypt(ECB_encrypt(profile_for('srivathsaeric@gmail.com','admin')))
