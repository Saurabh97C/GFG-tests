#User function Template for python3
class Solution:
	def minOperations(self, str1, str2):
		# code here
		n,m=len(str2),len(str1)
		
		dp=[[0]*(m+1) for _ in range(n+1)]
		
		for i in range(1,m+1):
		    dp[0][i]=i
		    
		for i in range(1,n+1):
		    dp[i][0]=i
		    
		
		for i in range(1,n+1):
		    for j in range(1,m+1):
		        
		        if str1[j-1]==str2[i-1]:
		            dp[i][j]=dp[i-1][j-1]
		        else:
		            dp[i][j]=min(dp[i][j-1],dp[i-1][j])+1
		            
		return dp[n][m]
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s1, s2 = input().split()
        ob = Solution()
        ans = ob.minOperations(s1, s2)
        print(ans)

# } Driver Code Ends