"""
Daily Coding Problem: Problem #4 [Hard]

Daily Coding Problem <founders@dailycodingproblem.com> Unsubscribe
Sep 2, 2019, 10:15 PM
to me

 Daily Coding Problem
Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

A= [3, 4, -1, 1, 4, 3]
A= [1, 2, 0]

def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True

    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n - x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True

    return arr

def first_missing_positive_integer(A):
    A = bubble_sort(A)

    for i in range(len(A)-1):
        if A[i] > 0 and A[i] != A[i+1]:
            if A[i] != (A[i+1]-1):
                return print(A[i]+1)
    return print(A[i+1]+1)

first_missing_positive_integer(A)