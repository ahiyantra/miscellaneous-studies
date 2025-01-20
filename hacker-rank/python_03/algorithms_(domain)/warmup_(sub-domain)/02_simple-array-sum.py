# https://www.hackerrank.com/challenges/simple-array-sum/problem

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
PrepareAlgorithmsWarmupSimple Array Sum
Simple Array Sum
9 more points to get your first star!
Rank: 3204344|Points: 21/30
Problem Solving
You have successfully solved Simple Array Sum  
You are now 9 points away from the 1st star for your problem solving badge.
Try the next challenge | Try a Random Challenge
Problem
Submissions
Leaderboard
Discussions
Editorial
HackerRank Logo
|
PrepareAlgorithmsWarmupSimple Array Sum
Exit Full Screen View
Problem	Submissions	Leaderboard	Discussions	Editorial
Given an array of integers, find the sum of its elements.

For example, if the array , , so return .

Function Description

Complete the simpleArraySum function in the editor below. It must return the sum of the array elements as an integer.

simpleArraySum has the following parameter(s):

ar: an array of integers
Input Format

The first line contains an integer, , denoting the size of the array.
The second line contains  space-separated integers representing the array's elements.

Constraints


Output Format

Print the sum of the array's elements as a single integer.

Sample Input

6
1 2 3 4 10 11
Sample Output

31
Explanation

We print the sum of the array's elements: .

Language
Python 3
More
1234567891011121314151617181920212223242526272829303132333435

    fptr.write(str(result) + '\n')

    fptr.close()

Line: 35 Col: 1

Test against custom input
Congratulations
You solved this challenge. Would you like to challenge your friends?Share on FacebookShare on TwitterShare on LinkedIn

Test case 0

Test case 1

Test case 2
Compiler Message
Success
Input (stdin)
6
1 2 3 4 10 11
Expected Output
31
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
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    # Write your code here
    v1 = 0
    for v0 in ar:
        v1 +=v0
    return v1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
