import random
import multiprocessing

"""
*** MULTIPROCESSING ***
Advantage:
- Advantage, if you have multiple CPUs core
- You can to kill the child processes.
- CPU-bound applications

Disadvantages:
- lot of memory used
- Not shared memory between process

"""

def list_append(count, id, out_list):
    for i in range(count):
        out_list.append(random.random())

if __name__ == "__main__":

    for xx in range(0, 5):
        # process
        size = 3000000
        procs = 8   #  We will run 8 processes

        jobs = []   # We will store all processes in a list.
        for i in range(0, procs):
            out_list = list()
            process = multiprocessing.Process(target=list_append, args=(size, i, out_list)) # Create a process object and set the constructor.
            jobs.append(process)    # Append processes to list

        # Start the processes (i.e. calculate the random number lists)
        for j in jobs:
            j.start()   # Start all processes

        # Ensure all of the processes have finished
        for j in jobs:
            j.join()    # If we use join, then the main process will be block.



