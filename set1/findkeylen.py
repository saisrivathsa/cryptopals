from ham_distance import hamdistance

def findingkeylen():
    file = open('6.txt')
    s = (''.join([line.strip() for line in file])).decode('base64')
    finalkeylen = 0
    score = 0
    for i in range(2,len(s)):
        scoretmp = 0
        j = 0
        while (j <= len(s)%i):
            scoretmp += hamdistance(s[j*i:i*(j+1)],s[i*(j+1):i*(j+2)])
            j = j+2
        scoretmp = scoretmp/i
        if scoretmp >= score:
            score = scoretmp
            finalkeylen = i
    return finalkeylen
