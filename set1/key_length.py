from ham_distance import *

def findkeylen(s):
    key_size = 1
    final_score = 0
    for key in range(1,40):
        normalized_score = 0.0
        for i in range(len(s)%key):
            normalized_score = normalized_score + hamdistance(s[key*i:(key+1)*i],s[(key+1)*i:(key+2)*i])
        normalized_score = normalized_score/key_size
        if final_score <= normalized_score:
            final_score = normalized_score
            key_size = key
    return key_size

if __name__ == "__main__" :
    file = open('6.txt')
    s = ("".join(line.strip() for line in file )).decode('base64')
    print findkeylen(s)
