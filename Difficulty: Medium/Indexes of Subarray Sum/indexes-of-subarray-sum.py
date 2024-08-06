#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
        if s==0:
            if 0 in arr:
                l=arr.index(0)
                return [l+1,l+1]
            else:
                return [-1]
        su=0
        strt=0
        for end in range(0,n):
            su+=arr[end]
            while su>s and strt<=end:
                su-=arr[strt]
                strt+=1
            if su==s:
                return [strt+1,end+1]
        return [-1]    



#{ 
 # Driver Code Starts.
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends