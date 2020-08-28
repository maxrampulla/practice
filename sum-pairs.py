def sum_pairs(ints, s):
  cache = set()
  for i in ints: 
    if s - i in cache:
      return [s-i, i]
      break
    cache.add(i)

    import math 

