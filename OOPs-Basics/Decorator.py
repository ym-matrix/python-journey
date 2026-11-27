import functools
import time 

start_time=time.time()

def performance(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        result=func(*args,**kwargs)
        end_time=time.time()
        elapsedtime=end_time-start_time
        return result,elapsedtime
    return wrapper

@performance
def sub(a,b):
    return a-b

print(sub(100,53))