alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def rot13(message):
  cache = []
  for char in list(message):
    if char.lower() in alpha:
      cache.append(helper(char, char.isupper()))
    else:
      cache.append(char)
  
  return "".join(cache)


def helper(char, isUpper):
  if isUpper:
    return alpha[(alpha.index(char.lower()) + 13) % 26].upper()
  else:
    return alpha[(alpha.index(char.lower()) + 13) % 26]