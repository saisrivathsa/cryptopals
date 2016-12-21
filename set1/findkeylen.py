from ham_distance import hamdistance

def normalize(s, length): #length is key length in question and data is the whole string in ascii
	norm_dist = 0
	for i in range (len(s)-(2*length)+1):
		norm_dist += hamdistance(s[i:i+length], s[i+length:i+2*length])
	norm_dist = (1.0*norm_dist)/((len(s)-(2*length)+1)*length)
	return norm_dist


def findingkeylen(string):
    finalkeylen = 0
    best_norm_dist = float('inf')
    for i in range (2, 100):
        tempdist = normalize(string, i)
        if tempdist <= best_norm_dist :
            best_norm_dist = tempdist
            finalkeylen = i
    return finalkeylen
