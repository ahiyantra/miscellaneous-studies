# https://www.hackerrank.com/challenges/mini-max-sum/problem

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
PrepareAlgorithmsWarmupMini-Max Sum
Mini-Max Sum
29 more points to get your next star!
Rank: 2110077|Points: 71/100
Problem Solving
Your Mini-Max Sum submission got 10.00 points.  
You are now 29 points away from the 2nd star for your problem solving badge.
Try the next challenge | Try a Random Challenge
Problem
Submissions
Leaderboard
Discussions
Editorial
HackerRank Logo
|
PrepareAlgorithmsWarmupMini-Max Sum
Exit Full Screen View
Problem	Submissions	Leaderboard	Discussions	Editorial
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Example

The minimum sum is  and the maximum sum is . The function prints

16 24
Function Description

Complete the miniMaxSum function in the editor below.

miniMaxSum has the following parameter(s):

arr: an array of  integers
Print

Print two space-separated integers on one line: the minimum sum and the maximum sum of  of  elements.

Input Format

A single line of five space-separated integers.

Constraints


Output Format

Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)

Sample Input

1 2 3 4 5
Sample Output

10 14
Explanation

The numbers are , , , , and . Calculate the following sums using four of the five integers:

Sum everything except , the sum is .
Sum everything except , the sum is .
Sum everything except , the sum is .
Sum everything except , the sum is .
Sum everything except , the sum is .
Hints: Beware of integer overflow! Use 64-bit Integer.

Need help to get started? Try the Solve Me First problem

Language
Python 3
More
12345678910111213141516282930313233172021221819232425262734
    maxRan = list(range(1,len(arr)-0))
    for v0 in minRan:
        minVal+=arr[v0]
    for v1 in maxRan:
        maxVal+=arr[v1]
    result = str(minVal) + " " + str(maxVal)
    print(result)

if __name__ == '__main__':


Line: 27 Col: 17

Test against custom input
Problem Solving
You have earned 10.00 points!
You are now 29 points away from the 2nd star for your problem solving badge.
59%71/100
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

Test case 9

Test case 10

Test case 11

Test case 12

Test case 13

Test case 14
Compiler Message
Success
Input (stdin)
1 2 3 4 5
Expected Output
10 14
BlogScoringEnvironmentFAQAbout UsSupportCareersTerms Of ServicePrivacy Policy
values, ``` ``` , Prints the values to a stream, or to sys.stdout by default. sep   string inserted between values, default a space. end   string appended after the last value, default a newline. file   a file-like object (stream); defaults to the current sys.stdout. flush   whether to forcibly flush the stream., hint

"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    minVal = 0
    maxVal = 0
    minRan = list(range(0,len(arr)-1))
    maxRan = list(range(1,len(arr)-0))
    for v0 in minRan:
        minVal+=arr[v0]
    for v1 in maxRan:
        maxVal+=arr[v1]
    result = str(minVal) + " " + str(maxVal)
    print(result)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
