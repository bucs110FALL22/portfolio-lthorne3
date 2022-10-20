score= int(input("What is your score out of 100? "))

def percentage_to_letter(score=0):
  if score >= 90: return "A"
  elif score >= 80: return "B"
  elif score >= 70: return "C"
  elif score >= 60: return "D"
  else : return "F"

letter= percentage_to_letter(score)

def is_passing(letter=None):
  if letter== "C":
    return True
  elif letter=="B":
    return True
  elif letter=="A":
    return True
  else:
    return False

  #also works: return letter in "ABC", returns a boolean

is_passing(letter)

if is_passing(letter)==True:
  print("You are passing.")
elif is_passing(letter)==False:
  print("You are failing")
  