""" 重复子序列   => 选与不选的问题
i -- list 指针
s -- 和
"""
arr=[3,34,4,12,5,2]

# recursion #

def rec_subset(arr, i, s):
    if s==o:
        return True
    elif i==0: 
        return arr[0]==s
    elif arr[i]>s:
        return rec_subset[arr, i-1, s]
    else: 
        A=rec_subset(arr, i-1, s-arr[i])
        B=rec_subset(arr, i-1, s)
        
        return A or B
        
   
   
   """非第归， 用二维数组保存动态过程
   https://www.youtube.com/watch?v=Jakbj4vaIbE  """
   import numpy as np
   def dp_subset(arr,s):
       subset=np.zeros((len(arr), s+1),dtype=bool) (行，列）
       subset[:,0]=True
       subset[0,:]=False                                        #subset[:,0] 所有行; subset[0,:] 所有列#
       subset[0，arr[0]]=True
       for i in range(1, len(arr)):
           for j in range(1, s+1):
               if arr[i]>s:
                  subset[i,s]=subset[i-1,s]
               else:
                  A=subset[i-1, s-i]
                  B=subset[i-1, s]
                  subset[i,s]=A or B
       r,c=subset.shape
       return subset[r-1,c-1]
             
             
   
