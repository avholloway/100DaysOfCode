# from flask import Flask
# app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return 'Hello, World!'


# if __name__ == "__main__":
#     app.run()


import time

def speed_calc_decorator1(function):
    start_time = time.time()
    function()
    print(f"{function.__name__} run time was {time.time()-start_time}")

def speed_calc_decorator2(function):
    def wrapper():
        start_time = time.time()
        function()
        print(f"{function.__name__} run time was {time.time()-start_time}")
    return wrapper

@speed_calc_decorator1
def fast_function():
    for i in range(10_000_000):
        i * i
        
@speed_calc_decorator2
def slow_function():
    for i in range(100_000_000):
        i * i

# fast_function() is auto executed
slow_function()