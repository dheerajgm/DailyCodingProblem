"""
Daily Coding Problem: Problem #27 [Easy]
Inbox
x

Daily Coding Problem <founders@dailycodingproblem.com> Unsubscribe
Wed, Sep 25, 9:52 PM (1 day ago)
to me

 Daily Coding Problem
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.


"""

S = "([])[]({()}{})"
S1 = "([)]"
S2 = "((()[]))"

A = S2

#  (    {    [
def bracketsbalanced(A):
    j = 1
    m = 0
    if len(A) == 1:
        return False
    sk = []
    for i in range(1,len(A)):
        if m != 0 and m == i:
            j = j +1
        for k in reversed(range(m,i)):
            if k in sk:
                continue
            prej = j
            if A[i] == ')' and A[k] == '(' or A[i] == '}' and A[k] == '{' or A[i] == ']' and A[k] == '[':
                sk.append(i)
                sk.append(k)
                j = j-1

                if j == 0:
                    m = i +1
                    break
                elif m > 0:
                    m = m
                    break
                else:
                    m = 0
                    break
            elif A[i] == ')' and A[k] == '[' or A[i] == '}' and A[k] == '(' or A[i] == ']' and A[k] == '}':
                return False

        if prej == j and m != i:
                j = j+1
    print(sk)

    return (True if j ==0 else False)

print(bracketsbalanced(A))