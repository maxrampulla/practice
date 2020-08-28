def encrypt_this(text):
  return " ".join("".join([str(ord(i[0])),i[len(i)-1],i[2:len(i)-1],i[1]]) if len(i) > 2 else "".join([str(ord(i[0])),i[1:]]) for i in text.split())