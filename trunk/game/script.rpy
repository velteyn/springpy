# You can place the script of your game in this file.

init:
    $ import subprocess as subprocess

    $ SPRING_DIR = "/spring"    # FIXME: replace with full directory for testing with SDK
    $ EXECUTABLE_DIR = SPRING_DIR + "/spring.exe"
    $ SCRIPT_FILENAME = "script_pwtest.txt"
    $ SCRIPT_DIR = SPRING_DIR + "/" + SCRIPT_FILENAME

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
    
    # TODO edit startscript to pass info to Spring
    
    "Launching spring.exe...{nw}"
    $ print(os.getcwd())
    $ subprocess.call([EXECUTABLE_DIR, SCRIPT_DIR])
    return
