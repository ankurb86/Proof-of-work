import hashlib
import timeit

def tGen(d):
    # Start Time for monitoring run time
    startTime = timeit.default_timer()

    #Generate Target with d '0' bits and remaining '1' bits
    d = int(d)
    target = ""
    for i in range(d):
        target = target + '0'
    for i in range(256-d):
        target = target + '1'
    print("\nTarget value = ", target)

    #Save target to a file
    f_target =open("../data/target.txt","w")
    f_target.write(target)
    f_target.close()

    # Check Execution time using the startTime variable
    stopTime = timeit.default_timer()
    print("\nThe run Time of the Target Generation Function is: ", stopTime - startTime)