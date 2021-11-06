list_bilangan = list(map(int, input().split(" ")))

def printList():
  for x in list_bilangan :
    if (x % 2 == 1):
      print (x, end = " ")
  print ()

printList()
list_bilangan[0] += 1
printList()