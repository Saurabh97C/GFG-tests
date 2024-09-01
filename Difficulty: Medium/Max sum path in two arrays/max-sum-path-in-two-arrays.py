#Your task is to complete this function
#Function should return an integer denoting the required answer
class Solution:
    def maxPathSum(self, arr1, arr2):
        # Code here
        s1=0
        s2=0
        ans=0
        i=0
        j=0
        m=len(arr1)
        n=len(arr2)

        while i<m and j<n:
            if arr1[i]==arr2[j]:
                ans+=max(s1, s2)+arr1[i]
                i+=1
                j+=1
                s1,s2=0,0
            elif arr1[i]<arr2[j]:
                s1+=arr1[i]
                i+=1
            else:
                s2+=arr2[j]
                j+=1
        
        while i<m:
            s1+=arr1[i]
            i+=1
        while j<n:
            s2+=arr2[j]
            j+=1
        
        return  ans+ max(s1, s2)

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxPathSum(arr1, arr2)
        print(ans)

# } Driver Code Ends