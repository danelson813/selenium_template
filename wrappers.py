#
#
# def logger(function):
#     def wrapper(*args, **kwargs):
#         print(f"----- {function.__name__}: start -----")
#         output = function(*args, **kwargs)
#         print(f"----- {function.__name__}: end -----")
#         return output
#     return wrapper
#
# @logger
# def some_function(text):
#     print(text)
#
# some_function("first test")
# # ----- some_function: start -----
# # first test
# # ----- some_function: end -----
#
# some_function("second test")
# # ----- some_function: start -----
# # second test
# # ----- some_function: end -----
#
#
# from functools import wraps
#
# def logger(function):
#     @wraps(function)
#     def wrapper(*args, **kwargs):
#         """wrapper documentation"""
#         print(f"----- {function.__name__}: start -----")
#         output = function(*args, **kwargs)
#         print(f"----- {function.__name__}: end -----")
#         return output
#     return wrapper
#
#
# import random
# import time
# from functools import lru_cache
#
#
# @lru_cache(maxsize=None)
# def heavy_processing(n):
#     sleep_time = n + random.random()
#     time.sleep(sleep_time)
#
# # first time
# %%time
# heavy_processing(0)
# # CPU times: user 363 µs, sys: 727 µs, total: 1.09 ms
# # Wall time: 694 ms
#
# # second time
# %%time
# heavy_processing(0)
# # CPU times: user 4 µs, sys: 0 ns, total: 4 µs
# # Wall time: 8.11 µs
#
# # third time
# %%time
# heavy_processing(0)
# # CPU times: user 5 µs, sys: 1 µs, total: 6 µs
# # Wall time: 7.15 µs
#
#
#
# from functools import wraps
#
# def cache(function):
#     @wraps(function)
#     def wrapper(*args, **kwargs):
#         cache_key = args + tuple(kwargs.items())
#         if cache_key in wrapper.cache:
#             output = wrapper.cache[cache_key]
#         else:
#             output = function(*args)
#             wrapper.cache[cache_key] = output
#         return output
#     wrapper.cache = dict()
#     return wrapper
#
# @cache
# def heavy_processing(n):
#     sleep_time = n + random.random()
#     time.sleep(sleep_time)
#
#
# %%time
# heavy_processing(1)
# # CPU times: user 446 µs, sys: 864 µs, total: 1.31 ms
# # Wall time: 1.06 s
#
# %%time
# heavy_processing(1)
# # CPU times: user 11 µs, sys: 0 ns, total: 11 µs
# # Wall time: 13.1 µs
#
#
# def repeat(number_of_times):
#     def decorate(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             for _ in range(number_of_times):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorate
#
#
# @repeat(5)
# def dummy():
#     print("hello")
#
# dummy()
# # hello
# # hello
# # hello
# # hello
# # hello
#
#
# import time
# from functools import wraps
#
# def timeit(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         result = func(*args, **kwargs)
#         end = time.perf_counter()
#         print(f'{func.__name__} took {end - start:.6f} seconds to complete')
#         return result
#     return wrapper
#
# @timeit
# def process_data():
#     time.sleep(1)
#
# process_data()
# # process_data took 1.000012 seconds to complete
#
#
#
# Write
# 1
#
# Dan Nelson
# Towards Data Science
# Published in
# Towards Data Science
#
# Ahmed Besbes
# Ahmed Besbes
# Feb 7
#
# ·
# 11 min read
# ·
#
# Member-only
#
# ·
#
# Listen
#
#
#
#
#
#
#
# BOOST YOUR PROGRAMMING SKILLS
# 12 Python Decorators to Take Your Code to the Next Level
# Do more things with less code without compromising on quality
#
# Photo by Chris Ried on Unsplash
# Python decorators are powerful tools that help you produce clean, reusable, and maintainable code.
#
# I’ve long waited to learn about these abstractions and now that I’ve acquired a solid understanding, I’m writing this story as a practical guide to help you, too, grasp the concepts behind these objects.
#
# No big intros or lengthy theoretical definitions today.
#
# This post is rather a documented list of 12 helpful decorators I regularly use in my projects to extend my code with extra functionalities.
# We’ll dive into each decorator, look at the code and play with some hands-on examples.
#
# If you’re a Python developer, this post will extend your toolbox with helpful scripts to increase your productivity and avoid code duplication.
#
# Less talk, I suggest we jump into the code now 💻.
#
# New to Medium? You can subscribe for $5 per month and unlock an unlimited number articles I write on programming, MLOps and system design to help data scientists (or ML engineers) produce better code.
#
# Join Medium with my referral link - Ahmed Besbes
# Read every story from Ahmed Besbes (and thousands of other writers on Medium). Your membership fee directly supports…
# ahmedbesbes.medium.com
#
# 1 — @logger (to get started)✏️
# If you’re new to decorators, you can think of them as functions that take functions as input and extend their functionalities without altering their primary purpose.
#
# Let’s start with a simple decorator that extends a function by logging when it starts and ends executing.
#
# The result of the function being decorated would look like this:
#
# some_function(args)
#
# # ----- some_function: start -----
# # some_function executing
# # ----- some_function: end -----
# To write this decroator, you first have to pick an appropriate name: let’s call it logger.
#
# logger is a function that takes a function as input and returns a function as output. The output function is usually an extended version of the input. In our case, we want the output function to surround the call of the input function with start and end statements.
#
# Since we don’t know what arguments the input function use, we can pass them from the wrapper function using *args and **kwargs. These expressions allow passing an arbitrary number of positional and keyword arguments.
#
# Here’s a simple implementation of the logger decorator:
#
# def logger(function):
#     def wrapper(*args, **kwargs):
#         print(f"----- {function.__name__}: start -----")
#         output = function(*args, **kwargs)
#         print(f"----- {function.__name__}: end -----")
#         return output
#     return wrapper
# Now you can apply logger to some_function or any other function for that matter.
#
# decorated_function = logger(some_function)
# Python provides a more pythonic syntax for this, it uses the @ symbol.
#
# @logger
# def some_function(text):
#     print(text)
#
# some_function("first test")
# # ----- some_function: start -----
# # first test
# # ----- some_function: end -----
#
# some_function("second test")
# # ----- some_function: start -----
# # second test
# # ----- some_function: end -----
# 2 — @wraps 🎁
# This decorator updates the wrapper function to look like the original function and inherit its name and properties.
#
# To understand what @wraps does and why you should use it, let’s take the previous decorator and apply it to a simple function that adds two numbers.
#
# (This decorator doesn’t use @wraps yet)
#
# def logger(function):
#     def wrapper(*args, **kwargs):
#         """wrapper documentation"""
#         print(f"----- {function.__name__}: start -----")
#         output = function(*args, **kwargs)
#         print(f"----- {function.__name__}: end -----")
#         return output
#     return wrapper
#
# @logger
# def add_two_numbers(a, b):
#     """this function adds two numbers"""
#     return a + b
# If we check the name and the documentation of the decorated function add_two_numbers by calling the __name__ and __doc__ attributes, we get … unnatural (and yet expected) results:
#
# add_two_numbers.__name__
# 'wrapper'
#
# add_two_numbers.__doc__
# 'wrapper documentation'
# We get the wrapper name and documentation instead ⚠️
#
# This is an undesirable result. We want to keep the original function’s name and documentation. That’s when the @wraps decorator comes in handy.
#
# All you have to do is decorate the wrapper function.
#
# from functools import wraps
#
# def logger(function):
#     @wraps(function)
#     def wrapper(*args, **kwargs):
#         """wrapper documentation"""
#         print(f"----- {function.__name__}: start -----")
#         output = function(*args, **kwargs)
#         print(f"----- {function.__name__}: end -----")
#         return output
#     return wrapper
#
# @logger
# def add_two_numbers(a, b):
#     """this function adds two numbers"""
#     return a + b
# By rechecking the name and the documentation, we see the original function’s metadata.
#
# add_two_numbers.__name__
# # 'add_two_numbers'
#
# add_two_numbers.__doc__
# # 'this function adds two numbers'
# 3 — @lru_cache 💨
# This is a built-in decorator that you can import from functools .
#
# It caches the return values of a function, using a least-recently-used (LRU) algorithm to discard the least-used values when the cache is full.
#
# I typically use this decorator for long-running tasks that don’t change the output with the same input like querying a database, requesting a static remote web page, or running some heavy processing.
#
# In the following example, I use lru_cache to decorate a function that simulates some processing. Then, I apply the function on the same input multiple times in a row.
#
# import random
# import time
# from functools import lru_cache
#
#
# @lru_cache(maxsize=None)
# def heavy_processing(n):
#     sleep_time = n + random.random()
#     time.sleep(sleep_time)
#
# # first time
# %%time
# heavy_processing(0)
# # CPU times: user 363 µs, sys: 727 µs, total: 1.09 ms
# # Wall time: 694 ms
#
# # second time
# %%time
# heavy_processing(0)
# # CPU times: user 4 µs, sys: 0 ns, total: 4 µs
# # Wall time: 8.11 µs
#
# # third time
# %%time
# heavy_processing(0)
# # CPU times: user 5 µs, sys: 1 µs, total: 6 µs
# # Wall time: 7.15 µs
# If you want to implement a cache decorator yourself from scratch, here’s how you’d do it:
#
# You add an empty dictionary as an attribute to the wrapper function to store previously computed values by the input function
# When calling the input function, you first check if its arguments are present in the cache. If it’s the case, return the result. Otherwise, compute it and put it in the cache.
# from functools import wraps
#
# def cache(function):
#     @wraps(function)
#     def wrapper(*args, **kwargs):
#         cache_key = args + tuple(kwargs.items())
#         if cache_key in wrapper.cache:
#             output = wrapper.cache[cache_key]
#         else:
#             output = function(*args)
#             wrapper.cache[cache_key] = output
#         return output
#     wrapper.cache = dict()
#     return wrapper
#
# @cache
# def heavy_processing(n):
#     sleep_time = n + random.random()
#     time.sleep(sleep_time)
#
#
# %%time
# heavy_processing(1)
# # CPU times: user 446 µs, sys: 864 µs, total: 1.31 ms
# # Wall time: 1.06 s
#
# %%time
# heavy_processing(1)
# # CPU times: user 11 µs, sys: 0 ns, total: 11 µs
# # Wall time: 13.1 µs
# 4 — @repeat 🔁
# This decorator causes a function to be called multiple times in a row.
#
# This can be useful for debugging purposes, stress tests, or automating the repetition of multiple tasks.
#
# Unlike the previous decorators, this one expects an input parameter.
#
# def repeat(number_of_times):
#     def decorate(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             for _ in range(number_of_times):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorate
# The following example defines a decorator called repeat that takes a number of times as an argument. The decorator then defines a function called wrapper that is wrapped around the function being decorated. The wrapper function calls the decorated function a number of times equal to the specified number.
#
# @repeat(5)
# def dummy():
#     print("hello")
#
# dummy()
# # hello
# # hello
# # hello
# # hello
# # hello
# 5 — @timeit ⏲️
# This decorator measures the execution time of a function and prints the result: this serves as debugging or monitoring.
#
# In the following snippet, the timeit decorator measures the time it takes for the process_data function to execute and prints out the elapsed time in seconds.
#
# import time
# from functools import wraps
#
# def timeit(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         result = func(*args, **kwargs)
#         end = time.perf_counter()
#         print(f'{func.__name__} took {end - start:.6f} seconds to complete')
#         return result
#     return wrapper
#
# @timeit
# def process_data():
#     time.sleep(1)
#
# process_data()
# # process_data took 1.000012 seconds to complete
# 6 — @retry 🔁
# This decorator forces a function to retry a number of times when it encounters an exception.
#
# It takes three arguments: the number of retries, the exception to catch and retry on, and the sleep time between retries.
#
# It works like this:
#
# The wrapper function starts a for-loop of num_retries iterations.
# At each iteration, it calls the input function in a try/except block. When the call is successful, it breaks the loop and returns the result. Otherwise, it sleeps for sleep_time seconds and proceeds to the next iteration.
# When the function call is not successful after the for loop ends, the wrapper function raises the exception.
# import random
# import time
# from functools import wraps
#
# def retry(num_retries, exception_to_check, sleep_time=0):
#     """
#     Decorator that retries the execution of a function if it raises a specific exception.
#     """
#     def decorate(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             for i in range(1, num_retries+1):
#                 try:
#                     return func(*args, **kwargs)
#                 except exception_to_check as e:
#                     print(f"{func.__name__} raised {e.__class__.__name__}. Retrying...")
#                     if i < num_retries:
#                         time.sleep(sleep_time)
#             # Raise the exception if the function was not successful after the specified number of retries
#             raise e
#         return wrapper
#     return decorate
#
# @retry(num_retries=3, exception_to_check=ValueError, sleep_time=1)
# def random_value():
#     value = random.randint(1, 5)
#     if value == 3:
#         raise ValueError("Value cannot be 3")
#     return value
#
# random_value()
# # random_value raised ValueError. Retrying...
# # 1
#
# random_value()
# # 5
#
#
# from functools import wraps
#
# def countcall(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         wrapper.count += 1
#         result = func(*args, **kwargs)
#         print(f'{func.__name__} has been called {wrapper.count} times')
#         return result
#     wrapper.count = 0
#     return wrapper
#
# @countcall
# def process_data():
#     pass
#
# process_data()
# process_data has been called 1 times
# process_data()
# process_data has been called 2 times
# process_data()
# process_data has been called 3 times
#
#
# import time
# from functools import wraps
#
# def rate_limited(max_per_second):
#     min_interval = 1.0 / float(max_per_second)
#     def decorate(func):
#         last_time_called = [0.0]
#         @wraps(func)
#         def rate_limited_function(*args, **kargs):
#             elapsed = time.perf_counter() - last_time_called[0]
#             left_to_wait = min_interval - elapsed
#             if left_to_wait > 0:
#                 time.sleep(left_to_wait)
#             ret = func(*args, **kargs)
#             last_time_called[0] = time.perf_counter()
#             return ret
#         return rate_limited_function
#     return decorate
#
#
#
# from dataclasses import dataclass,
#
# @dataclass
# class Person:
#     first_name: str
#     last_name: str
#     age: int
#     job: str
#
#     def __eq__(self, other):
#         if isinstance(other, Person):
#             return self.age == other.age
#         return NotImplemented
#
#     def __lt__(self, other):
#         if isinstance(other, Person):
#             return self.age < other.age
#         return NotImplemented
#
#
# john = Person(first_name="John",
#               last_name="Doe",
#               age=30,
#               job="doctor",)
#
# anne = Person(first_name="Anne",
#               last_name="Smith",
#               age=40,
#               job="software engineer",)
#
# print(john == anne)
# # False
#
# print(anne > john)
# # True
#
# asdict(anne)
# #{'first_name': 'Anne',
# # 'last_name': 'Smith',
# # 'age': 40,
# # 'job': 'software engineer'}
#
#
