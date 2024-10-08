
from typing import List


class Solution:
    def pairsum(self, arr : List[int]) -> int:
        maxi,smaxi=0,0
        for i in range(len(arr)):
            if arr[i]>maxi:
                maxi=arr[i]
        for i in range(len(arr)):
            if arr[i]>smaxi and arr[i]!=maxi:
                smaxi=arr[i]
        return maxi+smaxi# code here
        



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        arr = list(map(int, input().strip().split()))

        obj = Solution()
        res = obj.pairsum(arr)

        print(res)

# } Driver Code Ends