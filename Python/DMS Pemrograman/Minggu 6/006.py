def geser(key, text):
  hasil = ""
  for x in text:
    hasil += chr(ord(x) + key)
  return hasil

key = int(input())
p = input()