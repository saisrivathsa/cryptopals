from random import randint
from Crypto.Cipher import AES
from challenge_9 import pad

def random_key_generator(l=16):
    key = ''.join([chr(randint(0,255)) for i in range(l)])
    return key

def detection_oracle(data):
    c = 3
    if detect_ECB(pad(data)) :
        c = 1
    else :
        c = 0
    return c

def detect_ECB(data):
    for i in range(0,len(data)-16):
        for j in range(i+1,len(data)-16):
            if (data[i:i+16] == data[j:j+16]) :return True
    return False

def ECB_encrypt(data, key):
    l = len(data)
    b = randint(5,10)
    data = random_key_generator(b)+data+random_key_generator(randint(5,10))
    data = pad (data,16)
    mode = AES.new(key,AES.MODE_ECB)
    return mode.encrypt(data)[b:l+b]

def CBC_encrypt(data, key, IV):
    l = len(data)
    b = randint(5,10)
    data = random_key_generator(b)+data+random_key_generator(randint(5,10))
    data = pad (data, 16)
    encryptor = AES.new(key, AES.MODE_CBC, IV=IV)
    return encryptor.encrypt(data)[b:b+l]

def redirect():
    data = 'a'*8*16
    key = random_key_generator(16)
    IV = random_key_generator(16)
    c = randint(0,1)
    encrypted_data = ''
    if c == 0:
        encrypted_data = CBC_encrypt(data, key, IV)
    else :
        encrypted_data = ECB_encrypt(data, key)

    check = detection_oracle(encrypted_data)

    if c == check :
        print "Detection oracle succeeded",
        if c == 0:
            print "CBC detected"
        else :
            print "ECB detected"
    else :
        print "Detection oracle failed"

if __name__ == "__main__":
    redirect()
