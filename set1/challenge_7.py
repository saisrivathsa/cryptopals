from Crypto.Cipher import AES

def redirect(endodeddata,key):
    mode = AES.new(key,AES.MODE_ECB)
    decodeddata = mode.decrypt(encodeddata)
    return "\n"+decodeddata+"\n----------------------------------------------------------------------------------------------"


if __name__ == "__main__":
    file = open('7.txt')
    encodeddata = (''.join([line.strip() for line in file ])).decode('base64')
    key = "YELLOW SUBMARINE"
    print "\nDECODED DATA :\n-----------------------------------------------------------------------------------------------"
    print (redirect(encodeddata,key))
