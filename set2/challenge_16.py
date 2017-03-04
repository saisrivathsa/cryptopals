from Crypto.Cipher import AES

def random_key_generator(l=16):
    key = ''.join([chr(randint(0,255)) for i in range(l)])
    return key

IV = random_key_generator()
key = random_key_generator()

def pad(data):
    l = 16 - (len(data)%16)
    if l == 16: l = 0
    return data+chr(l)*l

def CBC_encrypt(data):
    cipher = AES.new(key, AES.MODE_CBC, IV=IV)
    return cipher.encrypt(data)

def CBC_decrypt(data):
    cipher = AES.new(key, AES.MODE_CBC, IV=IV)
    return cipher.decrypt(data)

def encryption(data):
    data = data.replace(';','').replace('=',';')
    return CBC_encrypt(pad("comment1=cooking%20MCs;userdata="+data+";comment2=%20like%20a%20pound%20of%20bacon"))

def admin_check(data) :
    return 'admin=True;' in data

if __name__ == "__main__":
    sample_encrypted = encryption('')
    attack_data = 'a'*16+'_admin_True_xxxx'
    attack_encrypted = encryption(attack_data)
    offset = 0
    for i in range(0,len(attack_encrypted),16) :
        if (sample_encrypted[i:i+16] == attack_encrypted[i:i+16]) : offset = i+16

    # offset is the index of the first '_' in  payload.
    # Similarly s_offset and t_offset correspond to the second and third '_' in the payload
    s_offset = offset+len('admin_')
    t_offset = s_offset+len('true_')

    attack_encrypted = list(attack_encrypted)
    attack_encrypted[offset] = chr(ord(attack_encrypted[offset]) ^ ord('_') ^ ord(';') )
    attack_encrypted[s_offset] = chr( ord(attack_encrypted[s_offset]) ^ ord('_') ^ ord('=') )
    attack_encrypted[t_offset] = chr( ord(attack_encrypted[t_offset]) ^ ord('_') ^ ord(';') )

    """
    The decrypted string of the block containing '_admin_True_xxxx' is xored with the previous cipher block to get the original string
    So we replace the elements corresponding to '_' in the previous cipher block in such a way that it produces ';' or '='

    If x is the corresponding element in previous cipher block

    x^'_' = e  ( e is encrypted text element)

    Replace e with e^'_'^';' So that when we finally retrieve the original data ';' will be added

    """

    attack_encrypted = ''.join(x for x in attack_encrypted)

    print "Attack successful" if admin_check(CBC_decrypt(attack_encrypted)) else "Attack failed"
