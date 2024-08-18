class Solution:
    def canSplit(self, arr):
        sumf,sumh=0,0
        if len(arr)==1:
            return False
        else:
            for i in arr:
                sumf+=i
            for i in arr:
                sumh+=i
                if sumh==sumf-sumh:
                    return True
            return False

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0])
    index = 1
    for _ in range(t):
        arr = list(map(int, data[index].split()))
        index += 1

        obj = Solution()
        res = obj.canSplit(arr)
        if (res):
            print("true")
        else:
            print("false")

# } Driver Code Ends