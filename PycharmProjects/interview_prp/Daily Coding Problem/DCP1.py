"""
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?


"""

A= [10, 15, 3, 7]
k = 17

def findpair(A, k):
    l = len(A)
    for i in range(l):
        for j in range(i+1, l):
            if k == (A[i] + A[j]):
                print('pair is '+ str(A[i]) + ' & '+ str(A[j]))
                return True

findpair(A, k)

def sumpair(A, k):
    pair = set()
    for i in A:
        if (k -i) in pair:
            print('fast pair is ' + str(i) + ' & ' + str(k-i))
            return True
        else:
            pair.add(i)

sumpair(A, k)