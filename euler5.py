# euler 5
# KeyJect
def isDiv(num):
  for i in range(2 , 21):
    if num%i!=0:
      return False
  return True

l = 2*3*5*7
i = 0
while True:
  i+=l
  if isDiv(i):
    print(i)
    break