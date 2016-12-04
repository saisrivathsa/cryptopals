from Crypto.Cipher import AES
from challenge_9 import pad

if __name__ == "__main__":
    file = open ('10.txt')
    data = pad((''.join([i.strip() for i in file])).decode('base64'),16)
    key = "YELLOW SUBMARINE"
    IV = 16 *'\x00'
    
    decryptor = AES.new(key, AES.MODE_CBC, IV=IV)
    print "\n" + decryptor.decrypt(data)
