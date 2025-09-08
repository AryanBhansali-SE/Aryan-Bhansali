'''An array is a data structure that stores elements of the same type in a contiguous block of memory. In an array, A
1, of size N, each memory location has some unique index, i (where
0 < i < N), that can be referenced as Ali] or Ai.
Your task is to reverse an array of integers.
Note: If you've already solved our C++ domain's Arrays Introduction challenge, you may
want to skip this.
Example
A = [1, 2, 3]
Return [3, 2, 1].
Function Description
Complete the function reverse Array with the following parameters):
• int An|: the array to reverse
Returns
• int n|: the reversed array
Input Format
The first line contains an integer, N, the number of integers in A.
The second line contains N space-separated integers that make up A.
Constraints
• 1≤N N≤ 103
• 1 ≤ Al] ≤ 104
, where Ali] is the ith integer in A'''


def reverseArray(a):
    a.reverse()
    return a

if __name__ == '__main__':
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)
    print(" ".join(map(str, res)))



