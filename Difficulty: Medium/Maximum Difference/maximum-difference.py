class Solution:
    def findMaxDiff(self, arr):
        n = len(arr)
        rightSmaller, leftSmaller = [0] * n, [0] * n
        stack = [arr[0]]
        for i in range(1, n):
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            rightSmaller[i] = stack[-1] if stack else 0
            stack.append(arr[i])
            
        stack2 = [arr[-1]]
        for i in range(n - 2, -1, -1):
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            leftSmaller[i] = stack[-1] if stack else 0
            stack.append(arr[i])
        
        maxDiff = float("-inf")
        for i, j in zip(leftSmaller, rightSmaller):
            maxDiff = max(maxDiff, abs(i - j))
        return maxDiff

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.findMaxDiff(arr))

# } Driver Code Ends