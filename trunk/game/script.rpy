# Code here is PUBLIC DOMAIN / CC-0; do whatever you like with it

init:
    python:
        import subprocess
        import sys
        import traceback
        
        SPRING_DIR = sys.path[0] + "/spring"           
        #SPRING_DIR = renpy.loader.transfn("../spring")
        EXECUTABLE_PATH = SPRING_DIR + "/spring.exe"
        SCRIPT_FILENAME = "script_pytest.txt"
        SCRIPT_PATH = SPRING_DIR + "/" + SCRIPT_FILENAME
        SCRIPT_FILENAME_TEMP = "_script.txt"
        SCRIPT_PATH_TEMP = SPRING_DIR + "/" + SCRIPT_FILENAME_TEMP
        RESULTS_PATH = SPRING_DIR + "/" + "results.py"
        RESULTS_PATH_COMPILED = SPRING_DIR + "/" + "results.pyo" # dunno if necessary to delete this as well
     
        sys.path.append(SPRING_DIR)
    
# The game starts here.
label start:
    call run_spring
    while True:
        # read our return file from Spring
        python:
            loadFromSpringSuccessful = False
            try:
                import results       # make sure this is the same as the file name of what your Spring gadget/widget outputs!
                reload(results)      # importing only works once, so reload is required for subsequent attempts to read module
                testValue = results.clock
                print(testValue)
                loadFromSpringSuccessful = True
            except:
                traceback.print_last()
                print("Failed to load data from Spring")
        if loadFromSpringSuccessful == True:
            "os.clock() value read as: [testValue]\nNow returning to main menu." 
            return
        
       
        menu:
            "Error loading combat results."
            "Abort":
                return
            "Retry":
                call run_spring
            "Ignore":
                return

label run_spring:
    
    # sample writing to startscript
    # for help see http://docs.python.org/2/tutorial/inputoutput.html
    python:
            # first get rid of the existing results file if there's one
            try:
                os.remove(RESULTS_PATH)
                os.remove(RESULTS_PATH_COMPILED)
            except:
                print("Warning: failed to delete results file(s)")
                print("File may already not exist, or may be in use")
            scriptRaw = open(SCRIPT_PATH, 'r')
            s = ""
            for line in scriptRaw:
                s += line
            s = s % {'playername': 'Threonine', 'ainame': 'Evil Bot'}
            scriptRaw.close()
            script = open(SCRIPT_PATH_TEMP, 'w')
            script.write(s)
            script.close()
    "Launching spring.exe...{nw}"
    $ subprocess.call([EXECUTABLE_PATH, SCRIPT_PATH_TEMP])
    return
