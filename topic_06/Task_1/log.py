def makeLog (a, b, operation, result, logfile = "log.txt") :
    try:
        file = open(logfile, "a")
        log_e = f"{a=}, {b=}, {operation=}, {result=}\n"
        file.write(log_e)
        file.close()
    except Exception as e:
        print(f'Error writing log, error is: {e}')