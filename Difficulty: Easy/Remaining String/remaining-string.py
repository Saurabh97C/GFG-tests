#User function Template for python3
class Solution:
    def printString(self, S, ch, count):
        c=0
        r=1
        if count==0:
            return S
        elif S.count(ch)<count:
            return ""
        for i in range(len(S)):
            if S[i]==ch:
                c=c+1
                if c==count:
                    r=i
        if S[r+1:]=="":
            return ""
        else:
            return S[r+1:]
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()
        ch = input()[0]
        count = int(input())
        ob = Solution()
        answer = ob.printString(s, ch, count)

        print(answer)

# } Driver Code Ends