def pad(string,length):
    l = length-(len(string)%length)
    return string+chr(l)*(l)

if __name__ == "__main__":
    string = "YELLOW SUBMARINE"
    length = 20
    print repr(pad(string,length))
