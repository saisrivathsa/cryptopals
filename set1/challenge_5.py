# The key 'ICE' is repeated to match the length of the string and later they are xored taking eacg character at a time

def xor(string,key):
    length = divmod(len(string),len(key))
    key = key*length[0]+key[0:length[1]]
    return ''.join([chr(ord(a)^ord(b)) for a,b in zip(string,key)])

if __name__ == "__main__":
    print (xor("\n".join([line.strip() for line in open('5.txt')]),"ICE")).encode('hex')
