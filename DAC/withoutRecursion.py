import random
import os
import time

def power(a, x):
    result = 1
    while x > 0:
        if x % 2 == 1:
            result *= a
        a *= a
        x //= 2
    return result

def measure_execution_time(test_case):
    start_time = time.time()
    a, x = test_case
    power(a, x)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

# Folder path for storing test cases and results
folder_path = "D:\CS112\DAC\TestCase_no_recursion"
if not os.path.exists(folder_path):
    os.mkdir(folder_path)

# Generate test cases and measure execution time
for i in range(7):  # Generate test cases with increasing digits from 1 to 9
    a = random.randint(10**(i+1), 10**(i+2)-1)  
    x = random.randint(10**(i+1), 10**(i+2)-1)  
    
    input_path = os.path.join(folder_path, f"Input{i + 1}.txt" )
    output_path = os.path.join(folder_path, f"Output{i + 1}.txt")
    test_case = (a, x)
    
    # Write test case to input file
    with open (input_path, "w") as file:
        file.write(" ".join(map(str, test_case)) + "\n")
        
    # Measure execution time
    execution_time = measure_execution_time(test_case)
    
    # Write execution time to output file
    with open (output_path, "w") as file:
        file.write(f"Time: {execution_time} seconds\n")
