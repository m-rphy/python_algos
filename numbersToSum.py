import math
import matplotlib.pyplot as plt


# Validate if a number is prime or not
def is_prime(number):
    if number <= 1:
        return False

    divisor = 2

    while divisor <= math.floor(math.sqrt(number)):
        if number % divisor == 0:
            return False
        divisor += 1

    return True


# This function finds the sum of all the digits in "num"
def digit_sum(num):
    sum = 0
    for digit in str(num):
        sum += int(digit)
    return sum


# To create a map of primes below 150
def map_primes():
    primes_map = {}
    arr = [0] * 150

    for el in range(len(arr)):
        if is_prime(el):
            primes_map[el] = el

    # print("this is the map of primes: ", primes_map)
    return primes_map


# If a digitSum is one of the first primes < 150, add it to dsPrimeMap
# I want to find a pattern for digitSum prime distribution
def prime_digit_sum():
    primes_map = map_primes()
    ds_prime_list = []

    N = 0
    D = 0

    while D < 1000:
        ds = digit_sum(N)
        if ds in primes_map:
            ds_prime_list.append(N)
            D += 1
        N += 1

    return ds_prime_list


def diff_calc(arr):
    result = []
    i = 0
    j = 1
    while i < len(arr) - 3:
        result.append(arr[j] - arr[i])
        i += 2
        j += 2

    return result


# arr = prime_digit_sum()
# print('difference Arr: ', diff_calc(arr))


# Plot the results of
def plot_diff_calc_results(arr):
    diff_result = diff_calc(arr)
    x_values = list(range(1, len(diff_result) + 1))

    plt.figure(figsize=(10, 6))
    plt.plot(x_values, diff_result, marker="o", linestyle="-", color="b")
    plt.xlabel("Index")
    plt.ylabel("Difference")
    plt.title("Difference Calculation Results")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    arr = prime_digit_sum()
    plot_diff_calc_results(arr)
