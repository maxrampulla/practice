def find_nb(m):
  counter = 0
  currentVolume = 0 

  while currentVolume < m:
    counter += 1
    currentVolume += counter**3
  
  if currentVolume != m:
    return -1
  else:
    return counter