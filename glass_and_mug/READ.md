### Glass and Mug Problem

You are given a glass with a capacity of G milliliters and a mug with a capacity of M milliliters, where G < M. Initially, both the glass and the mug are empty. You need to perform an operation K times, which consists of the following:

If the glass is full (i.e., contains exactly G milliliters), empty the glass.
If the mug is empty, fill the mug with M milliliters of water.
Transfer water from the mug to the glass until the glass is full or the mug is empty.
After performing these operations K times, print the amount of water in the glass and the mug.

Input Format
The first line contains three integers K, G, and M:
K: number of operations
G: glass capacity (in milliliters)
M: mug capacity (in milliliters)
Output Format
Print two integers representing the amount of water in the glass and the mug after K operations.
Sample Input
Copy code
5 300 500
Sample Output
Copy code
200 500