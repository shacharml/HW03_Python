
def fun2():

 vlst = ['x'+str(num) for num in range(10)]
 lamdic = {}
 for i,l in enumerate(vlst):
  lamdic.update({l: lambda x: x*j for j in range(1, i+2)})
 for v in vlst:
  for i in range(1,len(vlst)+1):
   print(lamdic[v](i),end=' ')
  print()

fun2()