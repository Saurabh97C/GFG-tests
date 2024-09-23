#User function Template for python3

class Solution:
    def findTwoElement( self,arr): 
        # code here
        arr1=[] #creating array of size n from 1 to n
        ans=[]
        seen=set()
        for i in range(len(arr)):
            arr1.append(i+1)
        diff=sorted(set(arr1)-set(arr)) # getting the number in arr1 not in arr

#finding the number which appeared more than once
        for i in arr:
            if i in seen:
                ans.append(i)
                break
            seen.add(i)
        ans.append(diff[0])
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findTwoElement(arr)
        print(str(ans[0]) + " " + str(ans[1]))
        tc = tc - 1

# } Driver Code Ends