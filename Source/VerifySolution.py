import hashlib
import timeit

def verifySol():
    # Start Time for monitoring run time
    startTime = timeit.default_timer()

    # Read Target 'target', Input 'message' and Solution 'solution' from files
    #Target
    f_target = open("../data/target.txt", "r")
    target = f_target.read()
    f_target.close()
    print("Target: ", target)
    #Message
    f_message = open("../data/input.txt", "r")
    message = f_message.read()
    f_message.close()
    print("Message: ", message)
    #Solution
    f_solution = open("../data/solution.txt", "r")
    solution = f_solution.read()
    f_solution.close()
    print("Solution: ", solution)

    #Compute the Hash value and verify with target
    nonce = int(solution,2)
    hash_val = hashlib.sha256(message.encode('utf-8') + str(nonce).encode('utf-8')).hexdigest()
    if int(hash_val,16) < int(target,2):
        print("Output: ",'1')
    else:
        print("Output: ", '0')

    # Check Execution time using the startTime variable
    stopTime = timeit.default_timer()
    print("\nThe run Time of the Solution Verification Function is: ", stopTime - startTime)