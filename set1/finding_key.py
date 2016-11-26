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
    score =  0
    key = ''
    for i in range(0,255):
        string =   "".join([chr(i^ord(j)) for j in s])
        scoretmp =   Score(string)
        if scoretmp >=   score:
            score = scoretmp
            key = i

    return chr(key)
