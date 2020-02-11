import sys
from TargetGeneration import tGen
from SolutionGeneration import sGen
from VerifySolution import verifySol
from TestRuns import mrun


if(sys.argv[1] == 'target'):
    tGen(sys.argv[2])
elif(sys.argv[1] == 'sol'):
    sGen()
elif(sys.argv[1] == 'verify'):
    verifySol()
elif(sys.argv[1] == 'multirun'):
    mrun()