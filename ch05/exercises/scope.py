#1
def mult(a, b): # prints a*b
  tot=0
  count=0
  for i in range(b):
    tot+= a
    count+=1
  return tot
  

#2
def power(x,y): #prints x^y
     res = 1 
     for i in range(y): 
         res *= x 
     return res 


#3- in main()


  

def main():
  a=5
  b=7
  print(mult(a,b))
  x=2
  y=3
  print(power(x,y))
  x=3
  print(power(x,2))

main()