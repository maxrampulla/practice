import math 

def list_squared(m, n):
  answers = []
  while m <= n:
    value = sumCheck(divisor(m, {1, m}))
    if isinstance(value, int):
      answers.append([m, value])
    m += 1
  return answers


def divisor(n, divisors):
  for x in range(2, n):
    if n % x == 0:
      divisors.add(x)
      divisor(n//x, divisors)
  return divisors

def sumCheck(list):
  cache = 0
  for i in list:
    cache += (i * i)
  if math.sqrt(cache) % 1 == 0: 
    return cache