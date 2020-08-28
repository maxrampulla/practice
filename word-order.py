def order(sentence):
  dict = {}
  words = 0
  cacheWord = ""
  cacheNumber = 0
  for i in (sentence + " "):
    if sentence == "":
      break
    elif i ==" ":
      dict[cacheNumber] = cacheWord
      words += 1
      cacheWord = ""
      cacheNumber = 0
    elif i.isdigit():
      cacheNumber = int(i)
      cacheWord += i
    else:
      cacheWord += i
  
  i = 1
  new = ""
  while i <= words:
    new = new + dict[i] + " "
    i += 1
  return new[:-1]