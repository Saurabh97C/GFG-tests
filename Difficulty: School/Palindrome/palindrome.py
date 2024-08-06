#User function Template for python3

class Solution:
    def is_palindrome(self, n):
       s=str(n)
       l=len(s)
       for i in range(n):
            if s[i]!=s[-(i+1)]:
                return("No")
                break
            else:
                return("Yes")
                break 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.is_palindrome(n)
		print(ans)
# } Driver Code Ends