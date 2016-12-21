def hamdistance(s1, s2):
    dist = 0
    # To convert all the characters to 8 bit binary
    ( ts1, ts2) = (''.join(['{0:08b}'.format(ord(i)) for i in s1]),''.join(['{0:08b}'.format(ord(i)) for i in s2]))
    for i,j in zip(ts1, ts2):
        if ( i != j ) :
            dist += 1
    return dist

if __name__ == "__main__":
    print hamdistance("this is a test","wokka wokka!!!")
