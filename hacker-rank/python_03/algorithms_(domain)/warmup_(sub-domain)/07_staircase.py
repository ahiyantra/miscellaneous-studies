# https://www.hackerrank.com/challenges/staircase/problem

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
PrepareAlgorithmsWarmupStaircase
Staircase
39 more points to get your next star!
Rank: 2257442|Points: 61/100
Problem Solving
Your Staircase submission got 10.00 points.  
You are now 39 points away from the 2nd star for your problem solving badge.
Try the next challenge | Try a Random Challenge
Problem
Submissions
Leaderboard
Discussions
Editorial
HackerRank Logo
|
PrepareAlgorithmsWarmupStaircase
Exit Full Screen View
Problem	Submissions	Leaderboard	Discussions	Editorial
Staircase detail

This is a staircase of size :

   #
  ##
 ###
####
Its base and height are both equal to . It is drawn using # symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of size .

Function Description

Complete the staircase function in the editor below.

staircase has the following parameter(s):

int n: an integer
Print

Print a staircase as described above.

Input Format

A single integer, , denoting the size of the staircase.

Constraints

 .

Output Format

Print a staircase of size  using # symbols and spaces.

Note: The last line must have  spaces in it.

Sample Input

6 
Sample Output

     #
    ##
   ###
  ####
 #####
######
Explanation

The staircase is right-aligned, composed of # symbols and spaces, and has a height and width of .

Language
Python 3
More
123456789101112131415162829303132171927182021262223242533
        dashes = "#" * ind
        if (ind != n):
            str2prnt = spaces + dashes
        else:
            str2prnt = dashes
        print(str2prnt)
        

if __name__ == '__main__':
    n = int(input().strip())

Line: 23 Col: 39

Test against custom input
Problem Solving
You have earned 10.00 points!
You are now 39 points away from the 2nd star for your problem solving badge.
44%61/100
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
95
Expected Output
                                                                                              #
                                                                                             ##
                                                                                            ###
                                                                                           ####
                                                                                          #####
                                                                                         ######
                                                                                        #######
                                                                                       ########
                                                                                      #########
                                                                                     ##########
                                                                {-truncated-}
Hidden Test Case
Use print or log statements to debug why your hidden test cases are failing. Hidden test cases are used to evaluate if your code can handle different scenarios, including corner cases.

BlogScoringEnvironmentFAQAbout UsSupportCareersTerms Of ServicePrivacy Policy
stop, ``` ``` , ``` range(stop) -> range object range(start, stop[, step]) -> range object ``` Return an object that produces a sequence of integers from start (inclusive) to stop (exclusive) by step. range(i, j) produces i, i+1, i+2, ..., j-1. start defaults to 0, and stop is omitted! range(4) produces 0, 1, 2, 3. These are exactly the valid indices for a list of 4 elements. When step is given, it specifies the increment (or decrement)., hint

"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    counter = list(range(1,n+1))
    str2prnt = ""
    for ind in counter:
        spaces = " " * (n-ind)
        dashes = "#" * ind
        if (ind != n):
            str2prnt = spaces + dashes
        else:
            str2prnt = dashes
        print(str2prnt)
        

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
