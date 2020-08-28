import string;
alphabet = {}

def initiate():
  counter = 1
  for i in string.ascii_lowercase:
    alphabet[i] = counter
    counter += 1


def high(x):
  initiate()
  cache = [0,""]
  for i in x.split():
    if cache[0] < value(i):
      cache = [value(i), i]
  return cache[1] 

def value(i):
  split = list(i)
  counter = 0
  for i in split:
    counter += alphabet[i]
  return counter