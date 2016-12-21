# The only change from challenge 12 is that another oracle is made which wraps the original oracle, removes the random
# prefix generated and returns the decoded text

from challenge_12modified import pad, unpad, AES_encrypt, check_ECB, find_block_size, next_chr, main, random_key_generator, randint, AES

key = random_key_generator()
prefix = random_key_generator(randint(20,50))

def byte_at_a_time_oracle(data):
    data = prefix + data + (("Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg\naGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq\ndXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg\nYnkK").decode('base64'))
    return AES_encrypt(data, True)

def remove_scrap(oracle):
    global proper_prefix , scrap
    # proper_prefix is the characters that must be added to the data to make up a complete block
    # scrap is the offset from where the data sent by used starts
    block_size = find_block_size(oracle)
    i = 0
    while True:
        check = oracle('A'*i)
        for j in range(0, len(check)-16, 16):
            if check[j:j+16] == check [j+16:j+32]:
                proper_prefix, scrap = ('A'*i, j+32)
                return 0
        i += 1

def new_oracle(data):
    return byte_at_a_time_oracle(proper_prefix + data)[scrap:]

if __name__ == "__main__" :
    remove_scrap(byte_at_a_time_oracle)
    main(new_oracle)
