'''
Daily Coding Problem: Problem #92 [Hard]
Inbox
x

Daily Coding Problem <founders@dailycodingproblem.com>
10:15 PM (36 minutes ago)
to me

 Daily Coding Problem
Good morning! Here's your coding interview problem for today.

This problem was asked by Airbnb.

We're given a hashmap associating each courseId key with a list of courseIds values, which represents that the
prerequisites of courseId are courseIds. Return a sorted ordering of courses such that we can finish all courses.

Return null if there is no such ordering.

For example, given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}, should return ['CSC100', 'CSC200', 'CSCS300'].
'''

A= { 'CSC200': ['CSC100'],'CSC300': ['CSC100', 'CSC200'], 'CSC100': []}

def all_courses(A):
    courses =[]
    for key, value in A.items():
        print(key)
        print(value)
        for val in value:
            if val not in courses:
                courses.append(val)
        if key not in courses:
            courses.append(key)
    return sorted(courses, key=lambda x: x)



print(all_courses(A))

