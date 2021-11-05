# pip install memory_profiler

# run it like the following
# python -m memory_profiler memory_profiler_expm.py
# make sure to uncomment the @profile

#@profile
def mem_func():
    lots_of_numbers = list(range(1500))
    x = ['letters'] * (5 ** 10)
    del lots_of_numbers
    return None

if __name__ == '__main__':
    mem_func()

# The memory_profiler also includes mprof which can be 
# used to create full memory usage reports over time 
# instead of line-by-line.

# $ mprof run  memory_profiler_expm.py
# again, don't forget to uncomment @profile