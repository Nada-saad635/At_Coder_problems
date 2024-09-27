### Problem Statement
You are given a string 
S of length 
N consisting of A, B, and C.
Find the position where ABC first appears as a (contiguous) substring in 
S. In other words, find the smallest integer 
n that satisfies all of the following conditions.

1≤n≤N−2.
The string obtained by extracting the 
n-th through 
(n+2)-th characters of 
S is ABC.
If ABC does not appear in 
S, print -1.

Constraints
3≤N≤100
S is a string of length 
N consisting of A, B, and C.
Input
The input is given from Standard Input in the following format:

N
S
Output
Print the position where ABC first appears as a substring in 
S, or -1 if it does not appear in 
S.

Sample Input 1
```bash
8
ABABCABC
```
Sample Output 1
3