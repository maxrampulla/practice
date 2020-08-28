def diamond(n):
  if n == 0 or n < 0 or (n % 2) == 0:
    return None
  else: 
    cache = [(n * "*")]
    i = n - 2
    while i > 0:
        cache.insert(0, (" " * int((n - i)/2)) + (i * "*"))
        cache.append((" " * int((n - i)/2)) + (i * "*"))
        i -= 2
    return "\n".join(cache) + "\n"
