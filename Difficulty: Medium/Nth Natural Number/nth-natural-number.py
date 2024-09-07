#User function Template for python3

class Solution:
    def findNth(self,n):
        result = []
        while n > 0:
            result.append(n % 9)
            n //= 9
        return int(''.join(map(str, result[::-1])))
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for i in range(0, t):
    n = int(input())
    obj = Solution()
    s = obj.findNth(n)
    print(s)

# } Driver Code Ends