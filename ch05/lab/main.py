def foo(n):
  count = 0
  nums=[n]
  for i in [nums]:
    if n%2==0:
      n=n/2
      count+=1
    else:
      n= (3*n)+1
      count+=1
    
    if n==1:
      break
    print(n)
    print("count =", count)
    return n
    
foo(101)

