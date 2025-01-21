# https://www.hackerrank.com/challenges/arrays-ds/problem

"""

HackerRank Home
|
Prepare
Certify
Compete
Apply
Search


|
Switch to..

ahiyantra
PrepareData StructuresArraysArrays - DS
Arrays - DS
94 more points to get your next star!
Rank: 1667730|Points: 106/200
Problem Solving
Your Arrays - DS submission got 10.00 points.  
You are now 94 points away from the 3rd star for your problem solving badge.
Try the next challenge | Try a Random Challenge
Problem
Submissions
Leaderboard
Discussions
Editorial
HackerRank Logo
|
PrepareData StructuresArraysArrays - DS
Exit Full Screen View
Problem	Submissions	Leaderboard	Discussions	Editorial
An array is a type of data structure that stores elements of the same type in a contiguous block of memory. In an array, , of size , each memory location has some unique index,  (where ), that can be referenced as  or .

Reverse an array of integers.

Note: If you've already solved our C++ domain's Arrays Introduction challenge, you may want to skip this.

Example

Return .

Function Description

Complete the function reverseArray in the editor below.

reverseArray has the following parameter(s):

int A[n]: the array to reverse
Returns

int[n]: the reversed array
Input Format

The first line contains an integer, , the number of integers in .
The second line contains  space-separated integers that make up .

Constraints

Sample Input 1

CopyDownload
Array: arr
1
4
3
2

 
4
1 4 3 2
Sample Output 1

2 3 4 1

Language
Python 3
More
1234567891011121314151617232425262728293031323334351820212219
        revArr[v0]=a[len(a)-1-v0]
    return revArr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))


Line: 22 Col: 18

Test against custom input
Problem Solving
You have earned 10.00 points!
You are now 94 points away from the 3rd star for your problem solving badge.
6%106/200
Congratulations
You solved this challenge. Would you like to challenge your friends?Share on FacebookShare on TwitterShare on LinkedIn

Test case 0

Test case 1

Test case 2

Test case 3

Test case 4

Test case 5

Test case 6

Test case 7

Test case 8
Compiler Message
Success
Input (stdin)
8
6676 3216 4063 8373 423 586 8850 6762
Expected Output
6762 8850 586 423 8373 4063 3216 6676
Hidden Test Case
Use print or log statements to debug why your hidden test cases are failing. Hidden test cases are used to evaluate if your code can handle different scenarios, including corner cases.

BlogScoringEnvironmentFAQAbout UsSupportCareersTerms Of ServicePrivacy Policy
No definition found

"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def reverseArray(a):
    # Write your code here
    revArr = list(range(0,len(a)))
    counter = list(range(0,len(a)))
    for v0 in counter:
        revArr[v0]=a[len(a)-1-v0]
    return revArr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
