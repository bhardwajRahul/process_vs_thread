import random
import threading

"""
*** MULTITHREADING ***
Advantage:
- Shared memory
- low memory usage
- I/O-bound applications (For example: networking)
- Easy UI (user interface) communications
- Access global variables.

Disadvantages:
- Not killable the child threads
- If you have one CPU core then not faster the code.
- Hard debug code.

"""

def list_append(count, id, out_list):
    for i in range(count):
        out_list.append(random.random())

if __name__ == "__main__":

    for xx in range(0, 5):
        # thread
        size = 3000000
        threads = 8     # We will run 8 threads
        jobs = []       # We will store all threads in a list.
        for i in range(0, threads):
            out_list = list()
            thread = threading.Thread(target=list_append(size, i, out_list))    # Create a thread object and set the constructor.
            jobs.append(thread) # Append threads to list.

        for j in jobs:
            j.start()   # Start all threads

        for j in jobs:
            j.join()    # If we use join, then the main thread will be block.



