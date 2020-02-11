import timeit
from TargetGeneration import tGen
from SolutionGeneration import sGen
from VerifySolution import verifySol

def mrun():
    for i in range(1,7):
        print('------------------------------------------')
        print('RUN ',i)
        print('------------------------------------------')
        # Start Time for monitoring run time
        startTime = timeit.default_timer()

        diff = i+20
        print("Difficulty: ",diff  )

        tGen(diff)
        sGen()
        verifySol()

        # Check Execution time using the startTime variable
        stopTime = timeit.default_timer()
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print("\n\nThe run Time of the Function for checking difficulty ",i," is: ", stopTime - startTime)

        # Save Stats
        fstats = open("../data/runstats.txt", "a+")
        fstats.write("Difficulty: ")
        fstats.write(str(diff))
        fstats.write(" Runtime: ")
        fstats.write(str(stopTime - startTime))
        fstats.write("\n")
        fstats.close()

        print('------------------------------------------')
        print('End of RUN ', i)
        print('------------------------------------------\n\n\n')