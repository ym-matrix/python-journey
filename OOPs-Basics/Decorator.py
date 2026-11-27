import functools
import time 

# Decorator that measures how long a function takes to run
def performance(func):
    # Preserve the original function's name and metadata
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        # Record the start time before calling the function
        start_time=time.time()
        # Call the original function with its arguments
        result=func(*args,**kwargs)
        # Record the end time and calculate elapsed time
        end_time=time.time()
        elapsedtime=end_time-start_time
        # Return the function result and elapsed time
        return result,elapsedtime
    return wrapper

# Apply the performance decorator to sub
@performance
def sub(a,b):
    return a-b

# Print the subtraction result and elapsed time
print(sub(1010,1))