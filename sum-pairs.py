def sum_pairs(ints, s):
  cache = set()
  for i in ints: 
    if s - i in cache:
      return [s-i, i]
      break
    cache.add(i)

    import math 


def list_squared(m, n):
  answers = []
  while m <= n:
    sumCheck(divisor(m, [1,m])
    m += 1
  return answers


def divisor(n, divisors):
  for x in range(2, n):
    if n % x == 0:
      divisor(n//x, divisors.append(x))
  return divisors

def sumCheck(list):
  cache = 0
  for i in list:
    cache += (i * i)
  if math.sqrt(cache) % 1 == 0: 
    return cache