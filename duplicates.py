def duplicate_count(text):
  text = text.lower()
  dict = {}
  for i in list(text):
    try:
      dict[i] += 1
    except: 
      dict[i] = 0

  counter = 0
  for i in dict:
    if dict[i] > 0:
      counter += 1
  
  return counter