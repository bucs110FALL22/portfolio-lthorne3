#Part 1
print(10*5)
print(10**2)
print(15/10) 
print(15//10) 
print(-15//10) 
print(15%10) 
print(10%15) 
print(0%10) 
print(10/15) #should be 2/3 or .6 repeating so the decimal should not terminate

#Part 2
rate= input("What is the current exchange rate for Euro to Dollar?")
rate= float(rate)
amount= input("What is the amount of currency to exchange?")
amount= float(amount)
total= amount*rate
result= total-3
print("You received $", result, "back.")

