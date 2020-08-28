# goes through list and counts indicated books
def stock_list(listOfArt, listOfCat):
  if len(listOfArt) == 0 or len(listOfCat) == 0:
    return ""
  else:
    dict = {}
    dict = initialize(listOfCat)
    dict = process(listOfArt, dict)
    return " - ".join([("(" + key + " : " + str(dict[key]) + ")") for key in dict])
    

# fills dict with Cats 
def initialize(listOfCat):
  dict = {}
  for i in listOfCat:
    dict[i] = 0
  return dict


# processes the listOfArts 
def process(listOfArt, dict):
  for i in listOfArt:
    if i[0] in dict.keys():
      dict[i[0]] += int(i.split()[1])
  return dict 


