from collections import deque

class Heapbackend(dict): # rename
  '''
    Functionality we want:
      1.  Lazy deletion
        a.
      2.  Pointer to where new element should be inserted,
        a.  ought to be list of locations so we remember where everything was lazily deleted
      3.  Smart len() that does len(self.values())
      4.
      5.
      6.
      7.
      8.
      9.
      10.
    I feel like there's a simpler way to do this sh!t.  But I'm not aware of it.
      11.
      12.
      13.
      14.
      15.
      16.
      17.
      18.
  '''
  def __init__(self, *args, **kwargs):
    self.holes=deque
    self.update(*args, **kwargs)
  def __getitem__(self, key):
    return dict.__getitem__(self, key)
  def __setitem__(self, key, val):
    dict.__setitem__(self, key, val)
  def pop(self,k,):
    # pointer to current "hole" should be updated












if __name__=="__main__":
  d=Heapbackend()
  for i in range(9):
    d[i]=i
  d.pop(2,None)
  d.pop(3,None)
  d.pop(6,None)
  print(d)
  print(len(d))
