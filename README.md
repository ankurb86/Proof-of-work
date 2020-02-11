# Proof-of-work
Cryptography Class Project to implement Proof-of-work with SHA256

README FILE

PROJECT ON PROOF-OF-WORK for CS 6058 DATA SECURITY AND PRIVACY, SPRING 2018,
by ANKUR BHATTACHARYA, MID #M12467767
bhattaar@mail.uc.edu
April 10th, 2018

[ABOUT THE PROJECT]
    This project generates a solution given a message such that the hash value of the message and solution is smaller than
    a target that is selected based on a given difficulty level.
    We will be using the SHA-256 hash function for this
    The difficulty decides how small the value of the target should be. The smaller the value of the target, the more difficult
    it is to compute a solution lesser than the target.

---------------------------------------------------------------------------------------------------------------------------
CONTENTS
I.      SYSTEM AND SOFTWARE REQUIREMENTS
II.     RUNNING THE PROGRAM AND PROGRAM DESCRIPTIONS
III.    FILES AND STRUCTURE
IV.     KNOWN ISSUES AND WORKAROUNDS

---------------------------------------------------------------------------------------------------------------------------
I.  SYSTEM AND SOFTWARE REQUIREMENTS

1.  Operating System: Windows 7, Windows 8, Windows 10
2.  Software: Python 3.6.3
    Please note that the latest version of python i.e. Python 3.6.3 is required to run this if you're using Windows 10.
    Download the latest version at https://www.python.org/downloads/release/python-363/
    While Installing, check the button to include the Path to Python in Environment Variables

---------------------------------------------------------------------------------------------------------------------------
II. RUNNING THE PROGRAM AND PROGRAM DESCRIPTIONS

    1. Open up a command prompt window
    2. Check if Python is installed
        2.a.  To get to the command line, open the Windows menu and type “cmd” in the search bar. Select Command Prompt from the search results.
              In the Command Prompt window, type the following and press Enter.
                python
              If Python is installed and in your path, then this command will run python.exe and show you the version number.
                C:\Users\Nighthawk>python
                Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
                Type "help", "copyright", "credits" or "license" for more information.
              If python is installed, then type the following command and press Enter
                exit()
              If python is not installed, you will see
                'python' is not recognized as an internal or external command, operable program or batch file.
              In that case, please install python from the steps provided above
    3.  Go to the program location path by issuing the cd command with the path of the program's src folder
                cd <path>
                e.g. C:\Users\Nighthawk>cd /d D:\Development\Python\UC\pow_m12467767\src
    4.  Run the following command to install the hashlib package
                pip install hashlib
                e.g. D:\Development\Python\UC\pow_m12467767\src>pip install hashlib
    5.  COMMANDS FOR RUNNING THE PROGRAM
        If you need to change the message at any time then open the data/plaintext.txt folder and edit the message.
        You can change the secret key from the data/key.txt as well for the ENCRYPTION PROGRAM

        Type the required commands and press enter
        5.a.    GENERATING A TARGET VALUE
                This program will take in a difficulty value from the command line and will generate a target based on this difficulty.
                The target will be saved in "../data/target.txt" file in binary format.
                It computes the time taken to perform this target generation function.
                Replace the value <d> with a numerical value to set the difficulty

                Command:
                    python pow.py target <d>
                Example:
                    python pow.py target 3

        5.b.    GENERATING THE SOLUTION
                This program will take the target value from the target.txt file, take the message from the input.txt file and then hash the
                message with different nonces - numbers used only once - to find a hash value that is less than the target value.
                The program makes use of the hashlib library and computes the hash function using SHA-256.
                The values are compared by transforming the hexadecimal hash value and the binary target value into decimal values.
                When the required hash value is found, the nonce is saved as a solution in the solution.txt file.

                Command:
                    python pow.py sol

        5.c     VERIFYING THE SOLUTION
                This program takes the target from the target.txt file, the solution from the solution.txt file and the message from the
                input.txt file. A hash value of the message and the solution is performed and then compared with the target value.
                The values are compared by transforming the hexadecimal hash value and the binary target value into decimal values.
                If the hash value is less than the target, the solution is valid and the system outputs the value '1'.
                If the hash value is more than the target, the solution is invalid and the system outputs the value '0'.

                Command:
                    python pow.py verify

        5.d.    RUNNING FOR MULTIPLE DIFFICULTIES FROM 21-26
                This program will generate target values for difficulties 21, 22, 23, 24, 25 and 26.
                It will take the message from input.txt and loop through different nonces and hash with the message to find solutions
                whose hash values when computed with the messages are less than their respective targets.
                It will also output the runtimes for finding the program for each run.
                The program will save the run stats in the runstats.txt file

                Command:
                    python pow.py multirun


---------------------------------------------------------------------------------------------------------------------------
III. FILES AND STRUCTURE

    The Files included in this project are:
    build
    data
    --input.txt
    --solution.txt
    --target.txt
    --runstats.txt
    src
    --pow.py
    --SolutionGeneration.py
    --TargetGeneration.py
    --TestRuns.py
    --VerifySolution.py
    Readme.txt

---------------------------------------------------------------------------------------------------------------------------
IV. KNOWN ISSUES AND WORKAROUNDS

    If you receive the below error at any point of time, then follow the steps provided below as a fix.

    [ISSUE 1]
    OSError: raw write() returned invalid length
    This error mostly pops up while running the VERIFY SOLUTION program.

    [WORKAROUND]
    This occurs if you're running Windows 10 and a version of Python lower than 3.6.
    Update your python version to 3.6+ to fix the issue.

    [ISSUE 2]
    ImportError: No module named hashlib
    This error mostly pops up while running the Solution Generation, Verify Solution and Multiple Difficulty run programs

    [WORKAROUND]
    This occurs if the hashlib package did not come installed with python.
    Install hashlib package with pip to fix the issue (Step II.4).

