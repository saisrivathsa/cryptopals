# ALL THE LINES ARE DECRYPTED JUST LIKE PREVIOUS CHALLENGE AND THE LINE WITH HIGHEST SCORE IS POSSIBLY THE CORRECT STRING 

from challenge_3 import Score

if __name__ == "__main__":
    file =  open('4.txt')
    score = 0
    final_string = ''
    for line in file :
        for i in range(256):
            string =   "".join([chr(i^ord(j)) for j in line.strip().decode('hex')])
            scoretmp = Score(string.lower())
            if scoretmp >= score:
                score = scoretmp
                final_string = string
    print final_string
