"""
Given an array of integers sorted in increasing order and a target, find the index of the first element in the array that is larger than or equal to the target. 
Assume that it is guaranteed to find a satisfying number.

Input:

    arr = [1, 3, 3, 5, 8, 8, 10]
    target = 2

Output: 1

Explanation: The first element larger than 2 is 3, which has index 1.

Input:

    arr = [2, 3, 5, 7, 11, 13, 17, 19]
    target = 6

Output: 3

Explanation: The first element larger than 6 is 7, which has index 3.

"""

def first_not_smaller(arr: list[int], target: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    l = 0
    r = len(arr)-1

    while l <= r:
        mid = (l+r) // 2
        
        if arr[mid] < target:
            l = mid + 1
            if arr[l+1] >= target:
                return l

        elif arr[mid] > target:
            r = mid - 1


    return 0

if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = first_not_smaller(arr, target)
    print(res)

