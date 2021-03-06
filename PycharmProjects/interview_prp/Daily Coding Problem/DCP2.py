""""
Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of 
all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input 
was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""
A = [1, 2, 3, 4, 5]
def mularrayelements(A):
    A1=[]
    l= len(A)
    for i in range(l):
        R=1
        for j in range(l):
            if i != j:
                R = R * A[j]
        A1.append(R)
    return A1

print(mularrayelements(A))

arr = A

def usingDivision(arr):
    product = 1
    for number in arr:
        product *= number

    prod = [product//x for x in arr]
    return prod

def withoutdivision(arr):
    l = len(arr)
    left = [1 for _ in range(l)]
    right = [1 for _ in range(l)]
    prod = [1 for _ in range(l)]

    for i in range(1,l):
        left[i] = arr[i-1] * left[i-1]

    for i in range(l-2, -1, -1):
        right[i] = arr[i+1] * right[i+1]

    for i in range(l):
        prod[i] = left[i] * right[i]

    return prod

usingDivision(arr)

withoutdivision(arr)