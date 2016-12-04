def pad(string,length):
    return string+"\x04"*(length-(len(string)%length))

if __name__ == "__main__":
    string = "YELLOW SUBMARINE"
    length = 20
    print repr(pad(string,length))
