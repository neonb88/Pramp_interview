# imports:
import numpy as np















#======================================================================











#======================================================================
def qsort(A, lo, hi):
  '''
    quicksort algorithm

    1.  pick pivot
    2.  sort the subArray around that pivot
  '''
  if lo < hi:
    p=partition(A, lo, hi)
    #print("pivot = "+str(p))
    return A # for testing purposes
    A=qsort(A,  lo,   p )
    A=qsort(A,  p+1,  hi)
  return A
#======================================================================         **43:10**

#======================================================================
def partition(A, lo, hi):
  #          median of lo,            mid,                     & hi 
  piv_val=np.median([A[lo],  A[ int(np.floor((lo+hi)/2)) ],    A[hi]])
  print("pivot value is "+str(piv_val))
  i=lo
  j=hi
  while True:
    while A[i] < piv_val:
      i+=1
      #print(" "*25+"i="+str(i))
    while A[j] > piv_val:
      j-=1
      #print(" "*41+"j="+str(j))
    if i >= j:
      #print("i="+str(i))
      #print("j="+str(j))
      return j

    # swap  (the actual sorting step)
    tmp=A[j]
    A[j]=A[i]
    A[i]=tmp
    #print("after swap, A="+str(A))
    #print("{0},     i={1}, A[{1}]={2},    j={3}, A[{3}]={4},    piv_val={5}".format(A, i,A[i], j,A[j], piv_val))
#======================================================================
    

#======================================================================
if __name__=="__main__":
  n=10
  #A = np.arange(n).astype('int64')
  #np.random.shuffle(A)
  #A = np.arange(n).astype('int64') +1
  #A=A[::-1]
  A=np.array([10,8,9,7,6,4,3,5,2,1]).astype('int64')
  #tmp=A[3]
  #A[3]=A[8]
  #A[8]=tmp
  print("initial array 'A'  :")
  print(A)
  A=qsort(A, 0, n-1)
  print(A)
#======================================================================











