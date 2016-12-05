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

if __name__ == "__main__":
    s1 = "ICE ICE BABY\x04\x04\x04\x04"
    s2 = "ICE ICE BABY\x05\x05\x05\x05"
    s3 = "ICE ICE BABY\x01\x02\x03\x04"
    print unpad(s1)
    print unpad(s2)
    print unpad(s3)
