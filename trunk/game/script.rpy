# You can place the script of your game in this file.

init:
    $ import subprocess as subprocess

    # sample script provided in SVN: trunk/spring
    # requires Zero-K v1.1.3.6 and map Green Comet Basic - edit script file if you want it to use something else 
    $ SPRING_DIR = "C:/Program Files/Spring"    # FIXME: replace with full directory for testing with SDK
    $ EXECUTABLE_DIR = SPRING_DIR + "/spring.exe"
    $ SCRIPT_FILENAME = "script_pytest.txt"
    $ SCRIPT_DIR = SPRING_DIR + "/" + SCRIPT_FILENAME
    $ SCRIPT_FILENAME_TEMP = "_script.txt"
    $ SCRIPT_DIR_TEMP = SPRING_DIR + "/" + SCRIPT_FILENAME_TEMP
    
# The game starts here.
label start:
    call run_spring
    while True:
        menu:

            # TODO parse a gadget/widget-written data file that tells us the results of combat

            "Combat complete, load data":
                $ print("a")
                return
             
            "Relaunch combat":
                $ print("b")
                call run_spring

            "Skip combat":
                $ print("c")
                return

label run_spring:
    
    # sample writing to startscript
    # for help see http://docs.python.org/2/tutorial/inputoutput.html
    python:
            scriptRaw = open(SCRIPT_DIR, 'r')
            s = ""
            for line in scriptRaw:
                s += line
            s = s % {'playername': 'Threonine', 'faction1': 'Dynasty'} # if you change playername Spring will exit with a "username not authorized to connect" error
            scriptRaw.close()
            script = open(SCRIPT_DIR_TEMP, 'w')
            script.write(s)
            script.close()
    "Launching spring.exe...{nw}"
    $ subprocess.call([EXECUTABLE_DIR, SCRIPT_DIR_TEMP])
    return
