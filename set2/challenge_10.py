from Crypto.Cipher import AES

def remove_gibberish(data):
    i = ord(data[len(data)-1])
    return data[:-i]

def xor(s1,s2):
    data = ''
    for i,j in zip(s1,s2):
        data += chr(ord(i)^ord(j))
    return data

def ECB_decrypt(data,key):
    mode = AES.new(key,AES.MODE_ECB)
    return mode.decrypt(data)

def CBC_decrypt(data,key,IV):
    prev_block = IV
    current_block = ''
    final_data = ''
    for i in range(len(data)/16):
        current_block = data[i*16:(i+1)*16]
        temp = ECB_decrypt(current_block,key)
        final_data += xor (temp,prev_block)
        prev_block = current_block
    return remove_gibberish(final_data)

if __name__ == "__main__":
    file = open('10.txt')
    data = (''.join([i.strip() for i in file])).decode('base64')
    key = "YELLOW SUBMARINE"
    IV = chr(0)*16
    print CBC_decrypt(data,key,IV)
