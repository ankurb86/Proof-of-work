import hashlib
import timeit
from random import randint
import binascii

def sGen():
    # Start Time for monitoring run time
    startTime = timeit.default_timer()

    #Read Target 'target' and Input 'message' from files
    f_target = open("../data/target.txt", "r")
    target =f_target.read()
    f_target.close()
    print("Target: ",target)
    f_message = open("../data/input.txt", "r")
    message = f_message.read()
    f_message.close()
    print("Message: ", message)

    #Keep generating solutions till we get Hash(message||solution)<target
    solution = ''
    max_nonce = 2**32
    for nonce in range(max_nonce):
        rnum = randint(1,10)
        hash_val = hashlib.sha256(message.encode('utf-8')+str(nonce+rnum).encode('utf-8')).hexdigest()
        if int(hash_val,16) < int(target,2):
            # solution = binascii.unhexlify(hash_val)
            #solution = bin(int(hash_val,16))[2:].zfill(256)
            nonce = nonce + rnum
            solution = bin(nonce)[2:].zfill(256)
            print("The Hash Value is: ",hash_val)
            break
    #print("Binary: ", solution)
    print("Solution value: ",int(solution,2))

    #Save the Solution
    f_solution = open("../data/solution.txt", "w")
    f_solution.write(solution)
    f_solution.close()

    # Check Execution time using the startTime variable
    stopTime = timeit.default_timer()
    print("\nThe run Time of the Solution Generation Function is: ", stopTime - startTime)