'''
The encrypted text is xored with all possible single byte keys and the resultant text is scored. The key which gave the
highest score is the possible key
'''
def Score(string):
  freq = dict()
  freq['a'] =  14810
  freq['b'] =  2715
  freq['c'] = 4943
  freq['d'] = 7874
  freq['e'] = 21912
  freq['f'] = 4200
  freq['g'] = 3693
  freq['h'] = 10795
  freq['i'] = 13318
  freq['j'] = 188
  freq['k'] = 1257
  freq['l'] = 7253
  freq['m'] = 4761
  freq['n'] = 12666
  freq['o'] = 14003
  freq['p'] = 3316
  freq['q'] = 205
  freq['r'] = 10977
  freq['s'] = 11450
  freq['t'] = 16587
  freq['u'] = 5246
  freq['v'] = 2019
  freq['w'] = 3819
  freq['x'] = 315
  freq['y'] = 3853
  freq['z'] = 128
  freq[' '] = 42320

  score= 0
  for i in string :
      if i in freq:
          score =  score+freq[i]
  return score

def redirect(s):
    final_string =  ""
    score =  0
    for i in range(0,255):
        string =   "".join([chr(i^ord(j)) for j in s])
        scoretmp =   Score(string)
        if scoretmp >=   score:
            score = scoretmp
            final_string = string
    print final_string

if __name__ == "__main__":
    s = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736".decode('hex')
    redirect(s)
