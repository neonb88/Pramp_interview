from collections import deque
import random, string

#=====================================================================
def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))
#=====================================================================


#=====================================================================
def longest_common_recur(src, targ, common):
  if len(src) == 0:
    return common
  elif len(targ) ==0:
    return common
  elif src[0]==targ[0]:
    return longest_common_recur(src[1:], targ[1:], common+targ[0])
  else:
    src_way   = longest_common_recur(src[1:], targ    , common)
    targ_way  = longest_common_recur(src    , targ[1:], common)
    if len(src_way) > len(targ_way):
      return src_way
    else:
      return targ_way
#=====================================================================
#=====================================================================
def diff_recurs(src, targ, common):
  '''
    TODO: edit this piece of shit.
  '''
  if len(src) == len(targ) == 0: # len(common) ALWAYS == 0    at this point
    return deque()
  if len(common)==0:
    if len(src) == 0:
      edits=diff_recurs(src,targ[1:],common)
      edits.appendleft('+'+targ[0])
      return edits
    elif len(targ)==0:
      edits=diff_recurs(src[1:],targ,common)
      edits.appendleft('-'+src[0])
      return edits
    else:
      edits=diff_recurs(src,targ[1:],common)
      edits.appendleft('+'+targ[0])
      return edits 
  else: # len(common) > 0, therefore len(src)>0 and len(targ)>0
    if common[0] == src[0] == targ[0]:
      edits=diff_recurs(src[1:],targ[1:],common[1:])
      edits.appendleft(common[0])
      return edits
    if common[0] == src[0]:
      edits=diff_recurs(src,targ[1:],common)
      edits.appendleft('+'+targ[0])
      return edits
    if common[0] == targ[0]:
      edits=diff_recurs(src[1:],targ,common)
      edits.appendleft('-'+src[0])
      return edits
    else:
      edits=diff_recurs(src,targ[1:],common)
      edits.appendleft('+'+targ[0])
      return edits 
#=====================================================================
#=====================================================================

    
#=====================================================================
#=====================================================================
def diffBetweenTwoStrings(source, target):   #diffBetweenTwoStrings(source, target):
  """
  @param source: str
  @param target: str
  @return: str[]
  """
  common_longest=longest_common_recur(source, target, '')
  print("common_longest"+common_longest)
  return list(diff_recurs(source, target, common_longest))

def test():
  for i in range(11):
    for test_case in range(22):
      print(diffBetweenTwoStrings(randomword(i),randomword(i)))
  '''
  print(diffBetweenTwoStrings('hi1t1', 'hi1t'))
  #print(diffBetweenTwoStrings('hiteruwqios', 'frehiitfhi'))
  #print(diffBetweenTwoStrings('hitherto ', 'theo'))  # NOTE: works
  print(diffBetweenTwoStrings('hitherto ', 'theos'))  # NOTE: breaks
  '''
test()
'''
  common_i=0
  src_i=0
  targ_i=0
  while common_i < len(common_longest):
    print("out:"+str(out))
    while src_i < len(source) and  source[src_i]  != common_longest[common_i]:
      out.append('-'+source[src_i])
      src_i+=1
    print('out:'+str(out))
    while targ_i < len(target) and target[targ_i] != common_longest[common_i]:
      out.append('+'+target[targ_i])
      targ_i+=1
    print('out:'+str(out))
    if common_longest[common_i] == source[src_i] == target[targ_i]:
      out.append(source[src_i])
      src_i+=1
      targ_i+=1
    print('out:'+str(out))
    common_i+=1
  return out
'''
  # TODO: print instructions, given longest_common_substr, source, and target.
#=====================================================================
#=====================================================================




  #1st  we can cut out all letters in the src which are NOT in the targ.
  #2nd  we must add letter in the targ which are NOT in the src.
  #3rd  we have to deal with reordering.  This part will be the weirdest (ie. "kittycat" => "tick")
    # A.  In this case (kittycat => tick), we'd have to look for the longest common substring.  kitct => "tc" is the longest common substring.
    # B.  But how did I find the longest common substring?
    # C.  The naive approach is to foreach thru the source string   and check 1st instance of char in target string.   Then we split into yet ANOTHER branch and foreach thru the targ string with c2=source[1]   to see whether
    
    # D. How did I literally approach the problem?  1) I found all the letters in common.    2) I counted up the longest common substring among the common letters.  But how did I actually do that?  I think I tested each letter from the 1st common substring, then from the 2nd, etc.

    # E. Theoretically there might be a way to do this with only 1 pass through the source string   and 1 pass through the targ string.  Maybe if we look at the shorter string 1st?  Or the shorter string of all common chars?  
    
    
    
    # Hash table all the chars in both strings and 
  
  # A.  In this case (kittycat => tick), we'd have to look for the longest common substring.  kitct => "tc" is the longest common substring.
#=====================================================================
   
#diff_strs
'''
#=====================================================================
def longest_common_recur(src, targ, common):
  if len(src) == 0:
    return common
  elif len(targ) ==0:
    return common
  elif src[0]==targ[0]:
    return longest_common_recur(src[1:], targ[1:], common+targ[0])
  else:
    src_way   = longest_common_recur(src[1:], targ    , common)
    targ_way  = longest_common_recur(src    , targ[1:], common)
    if len(src_way) > len(targ_way):
      return src_way
    else:
      return targ_way
#=====================================================================
def diffBetweenTwoStrings(source, target):   #diffBetweenTwoStrings(source, target):
  """
  @param source: str
  @param target: str
  @return: str[]
  """
  out=[]
  common_longest=longest_common_recur(source, target, '')
  common_i  = 0
  src_i     = 0
  targ_i    = 0
  while not (src_i >= len(source) and targ_i >=len(target) and common_i>=len(common_longest)):
    in_common=common_i < len(common_longest)
    while src_i < len(source) and in_common and source[src_i]  != common_longest[common_i]:
      out.append('-'+source[src_i])
      src_i+=1
    while targ_i < len(target) and in_common and target[targ_i] != common_longest[common_i]:
      out.append('+'+target[targ_i])
      targ_i+=1
    if in_common and common_longest[common_i] == source[src_i] == target[targ_i]:
      out.append(source[src_i])
      src_i+=1
      targ_i+=1
      common_i+=1
  return out
  # TODO: print instructions, given longest_common_substr, source, and target.
#=====================================================================




  #1st  we can cut out all letters in the src which are NOT in the targ.
  #2nd  we must add letter in the targ which are NOT in the src.
  #3rd  we have to deal with reordering.  This part will be the weirdest (ie. "kittycat" => "tick")
    # A.  In this case (kittycat => tick), we'd have to look for the longest common substring.  kitct => "tc" is the longest common substring.
    # B.  But how did I find the longest common substring?
    # C.  The naive approach is to foreach thru the source string   and check 1st instance of char in target string.   Then we split into yet ANOTHER branch and foreach thru the targ string with c2=source[1]   to see whether

    # D. How did I literally approach the problem?  1) I found all the letters in common.    2) I counted up the longest common substring among the common letters.  But how did I actually do that?  I think I tested each letter from the 1st common substring, then from the 2nd, etc.

    # E. Theoretically there might be a way to do this with only 1 pass through the source string   and 1 pass through the targ string.  Maybe if we look at the shorter string 1st?  Or the shorter string of all common chars?  



    # Hash table all the chars in both strings and 

  # A.  In this case (kittycat => tick), we'd have to look for the longest common substring.  kitct => "tc" is the longest common substring.
#=====================================================================

'''
