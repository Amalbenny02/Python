import math
def nPr(n,r):
  return math.factorial(n)/math.factorial(n-r)


n=int(input("Enter n:"))
r=int(input("Enter r:"))

result=nPr(n,r)
print("nPr:",result)
