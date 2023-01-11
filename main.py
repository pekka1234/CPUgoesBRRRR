from multiprocessing import Process

print("WARNING: DO NOT LET THIS RUN FOR TOO LONG")

def loop():
    while 1:
        pass

while 1:
    Process(target=loop).start()