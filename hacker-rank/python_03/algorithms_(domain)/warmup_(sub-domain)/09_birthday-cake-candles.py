# https://www.hackerrank.com/challenges/birthday-cake-candles/problem

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
PrepareAlgorithmsWarmupBirthday Cake Candles
Birthday Cake Candles
19 more points to get your next star!
Rank: 1975479|Points: 81/100
Problem Solving
Your Birthday Cake Candles submission got 10.00 points.  
You are now 19 points away from the 2nd star for your problem solving badge.
Try the next challenge | Try a Random Challenge
Problem
Submissions
Leaderboard
Discussions
Editorial
HackerRank Logo
|
PrepareAlgorithmsWarmupBirthday Cake Candles
Exit Full Screen View
Problem	Submissions	Leaderboard	Discussions	Editorial
You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of their total age. They will only be able to blow out the tallest of the candles. Count how many candles are tallest.

Example


The maximum height candles are  units high. There are  of them, so return .

Function Description

Complete the function birthdayCakeCandles in the editor below.

birthdayCakeCandles has the following parameter(s):

int candles[n]: the candle heights
Returns

int: the number of candles that are tallest
Input Format

The first line contains a single integer, , the size of .
The second line contains  space-separated integers, where each integer  describes the height of .

Constraints

Sample Input 0

4
3 2 1 3
Sample Output 0

2
Explanation 0

Candle heights are . The tallest candles are  units, and there are  of them.

Language
Python 3
More
1234567891011121314151617262728293031323334351819202221232425
    result=0
    for v0 in candles:
        if v0==tallest:
            result+=1
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

Line: 25 Col: 18

Test against custom input
Problem Solving
You have earned 10.00 points!
You are now 19 points away from the 2nd star for your problem solving badge.
73%81/100
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
4
3 2 1 3
Expected Output
2
BlogScoringEnvironmentFAQAbout UsSupportCareersTerms Of ServicePrivacy Policy
key, ``` ``` , ``` ``` , hint

"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    number=len(candles)
    candles.sort()
    tallest=candles[-1]
    result=0
    for v0 in candles:
        if v0==tallest:
            result+=1
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
