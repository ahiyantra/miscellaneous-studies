# https://www.hackerrank.com/challenges/time-conversion/problem

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
PrepareAlgorithmsWarmupTime Conversion
Time Conversion
4 more points to get your next star!
Rank: 1791936|Points: 96/100
Problem Solving
Your Time Conversion submission got 15.00 points.  
You are now 4 points away from the 2nd star for your problem solving badge.
Try the next challenge
Problem
Submissions
Leaderboard
Discussions
Editorial
HackerRank Logo
|
PrepareAlgorithmsWarmupTime Conversion
Exit Full Screen View
Problem	Submissions	Leaderboard	Discussions	Editorial
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example


Return '12:01:00'.


Return '00:01:00'.

Function Description

Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

timeConversion has the following parameter(s):

string s: a time in  hour format
Returns

string: the time in  hour format
Input Format

A single string  that represents a time in -hour clock format (i.e.:  or ).

Constraints

All input times are valid
Sample Input 0

07:05:45PM
Sample Output 0

19:05:45
Language
Python 3
More
1234567891011121314151617333418262720321928292122232425303135
        result=s[0:-2]
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)


Line: 31 Col: 23

Test against custom input
Problem Solving
You have earned 15.00 points!
You are now 4 points away from the 2nd star for your problem solving badge.
94%96/100
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
Compiler Message
Success
Input (stdin)
07:05:45PM
Expected Output
19:05:45
BlogScoringEnvironmentFAQAbout UsSupportCareersTerms Of ServicePrivacy Policy
obj, ``` ``` , Return the number of items in a container., hint

"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    amVsPm=s[-2:len(s)]
    firstTwoChars=s[0:2]
    firstTwoInts=int(firstTwoChars)
    if s[0:2]=="12" and amVsPm=="AM":
        result=s[2:-2]
        result="00"+result
    if s[0:2]=="12" and amVsPm=="PM":
        result=s[0:-2]
    if s[0:2]!="12" and amVsPm=="PM":
        firstTwoInts+=12
        result=s[2:-2]
        result=str(firstTwoInts)+result
    if s[0:2]!="12" and amVsPm=="AM":
        result=s[0:-2]
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
