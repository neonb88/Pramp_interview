import numpy as np

def pn(n=0):
  print('\n'*n)
#=====================================================================

n=5
np.random.seed(1)
a = np.arange(n).astype('int64')
np.random.shuffle(a)
print(a)
print("len(a) = "+str(n));pn()

# Sort an array a[0...n-1].
gaps = [701, 301, 132, 57, 23, 10, 4, 1]

#=====================================================================
# Start with the largest gap and work down to a gap of 1
for gap in gaps:
  # Do a gapped insertion sort for this gap size.
  # The first gap elements a[0..gap-1] are already in gapped order
  # keep adding one more element until the entire array is gap sorted
  for i in range(gap,n):
    print("gap = "+str(gap))
    print('i='+str(i))
    # add a[i] to the elements that have been gap sorted
    # save a[i] in temp and make a hole at position i
    temp = a[i]
    # shift earlier gap-sorted elements up until the correct location for a[i] is found
    j=i
    print("a[j-gap]:"+str(a[j-gap]))
    print("j="+str(j))
    while j>=gap and a[j-gap] > temp:
      print('j='+str(j))
      a[j] = a[j - gap]
      print(a)
      j-=gap
    # put temp (the original a[i]) in its correct location
    a[j] = temp
    print(a)
#=====================================================================
print(a)





































































