from challenge_11 import random_key_generator
from Crypto.Cipher import AES
from random import randint

key = random_key_generator()

def pad(string, length = 16):
    l = length-(len(string)%length)
    return string+chr(l)*(l)

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

def AES_encrypt(data, flag = False):
    cipher = AES.new(key, AES.MODE_ECB)
    if flag :
        data = pad(data)
    return cipher.encrypt(data)

def check_ECB(oracle, block_size):
    data = random_key_generator(randint(0,10))+'A'*block_size*2+random_key_generator(randint(0,30))+'A'*randint(2,5)*block_size
    encrypted_data = oracle(data)
    for i in range ((len(encrypted_data)/16)):
        for j in range(i+1,(len(encrypted_data)/16)):
            if encrypted_data[i*16:(i+1)*16] == encrypted_data[j*16:(j+1)*16]:
                return True
    return False

def find_block_size(oracle):
    test = 'A'
    l = len(oracle(test))
    while True :
        test += 'A'
        tmp_len = len(oracle(test))
        if tmp_len > l :
            return tmp_len - l

def byte_at_a_time_oracle(data):
    data += (("Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg\naGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq\ndXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg\nYnkK").decode('base64'))
    return AES_encrypt(data, True)

def next_chr(oracle, block_size, known):
    test_block_len = (block_size-1-len(known))%block_size
    test = 'A'*test_block_len
    check = oracle(test)[:len(test+known)+1]
    for i in range(256):
        tmp = oracle(test+known+chr(i))[:len(test+known)+1]
        if (tmp == check):
            return chr(i)

def main(oracle):
    block_size = find_block_size(oracle)
    if check_ECB(oracle, block_size):
        print "------------------------------------\nTHE ORACLE FUNCTION IS USING ECB\n------------------------------------\n"
    else :
        print "------------------------------\nUNABLE TO DETECT ECB IN ORACLE FUNCTION\n------------------------------\n"
    known = ''
    for i in range(0,len(oracle(''))):
        try:
            known += next_chr(oracle, block_size, known)
        except :
            break
    print unpad(known)

if __name__ == "__main__" :
    oracle = byte_at_a_time_oracle
    main(oracle)
