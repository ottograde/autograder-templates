import subprocess
import os
import time

# Import the student's solution from /student/fibonacci.py
import importlib.util


def load_module_from_file(file_path, module_name):
    # Create a new module specification
    spec = importlib.util.spec_from_file_location(module_name, file_path)

    # Load the module based on the specification
    module = importlib.util.module_from_spec(spec)

    # Execute the module code
    spec.loader.exec_module(module)

    return module


student_fibonacci = load_module_from_file("/student/fibonacci.py", "fibonacci")

if student_fibonacci.fibonacci(1) == 1:
    print("Test 1 passed")

time.sleep(2)

if student_fibonacci.fibonacci(2) == 1:
    print("Test 2 passed")

time.sleep(2)

if student_fibonacci.fibonacci(3) == 2:
    print("Test 3 passed")

time.sleep(2)

if student_fibonacci.fibonacci(10) == 55:
    print("Test 4 passed")

time.sleep(2)

if student_fibonacci.fibonacci(20) == 6765:
    print("Test 5 passed")

time.sleep(1)

if student_fibonacci.fibonacci(30) == 832040:
    print("Test 6 passed")
