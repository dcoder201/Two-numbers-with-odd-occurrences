#User function Template for python3
class Solution:
    def twoOddNum(self, Arr, N):
        # code here
        d=dict()
        res=[]
        for i in Arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for val in d.keys():
            if d[val]%2!=0:
                res.append(val)
        res.sort(reverse=True)
        return res



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        ob = Solution();
        ans = ob.twoOddNum(Arr,N)
        for i in range(len(ans)):
        	print(ans[i], end = " ")
        print()
# } Driver Code Ends
