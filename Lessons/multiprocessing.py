#Multiprocessing in Python: Multiprocessing is a Python module that provides a simple way to run multiple processes in parallel.


#Importing Multiprocessing:
import multiprocessing

#Creating a process:
import multiprocessing
def my_func():
  print("Hello from process", multiprocessing.current_process().name)
  process = multiprocessing.Process(target=my_func)
  process.start()
  process.join()
