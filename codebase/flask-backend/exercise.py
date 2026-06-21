import time

current_time = time.time()
print(current_time)  # seconds since Jan 1st, 1970

def speed_calc_decorator(func):
    def wrapper_function(*args, **kwargs):
        """
        Using *args and **kwargs inside your decorator's wrapper function allows it to accept any number of arguments,
        making your decorator universal. Without them, your decorator would break the moment you try to use it on a
        function that requires inputs.
        """
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} run speed: {end_time - start_time}s")
        return result
    return wrapper_function

@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i

fast_function()
slow_function()

