import time
import random
import os

def random_array(n):
    return [random.randint(1, 100000) for _ in range(n)]

def sum_even(arr):
    sum = 0
    for i in arr:
        sum += i
    return (sum % 2 == 0)

def generate_subsets(arr):
    subsets = []
    n = len(arr)
    # Duyệt qua tất cả các tập con có thể 2^n
    for i in range(1, 2**n):
        subset = []
        for j in range(n):
            # Kiểm tra xem phần tử thứ j có thuộc tập con không
            if (i >> j) & 1:
                subset.append(arr[j])
        subsets.append(subset)
    return subsets

def bruteforce(array):
    cnt = 0
    results = []
    n = len(array)
    all_subsets = generate_subsets(array)
    for subset in all_subsets:
        if sum_even(subset):
            cnt += 1
            results.append(subset)
    return cnt, results

def measure_execution_time(algorithm, test_case):
    start_time = time.time()
    cnt, results = algorithm(test_case)
    end_time = time.time()
    return cnt, results, end_time - start_time

n_values = [0, 1 , 5, 10, 15, 20, 25, 30]

for i, n in enumerate(n_values):
    folder_path = "D:\CS112\Bài tập 1\TestCase"
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    input_path = os.path.join(folder_path, f"Input{i + 1}.txt" )
    output_path = os.path.join(folder_path, f"Output{i + 1}.txt")
    test_case = random_array(n)
    with open (input_path, "w") as file:
        file.write(str(n) + "\n")
        file.write(" ".join(map(str, test_case)) + "\n")
        file.close()
    # print(test_case)
    cnt, results, bruteforce_time = measure_execution_time(bruteforce, test_case)
    with open (output_path, "w") as file:
        file.write(f"Count: {cnt}" + "\n")
        file.write(f"Time: {bruteforce_time}" + "\n")
        file.close()