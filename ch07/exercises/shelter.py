import time

class Animal:
  def __init__ (self, name, type):
    self.name= name
    self.type= type
    self.id= time.strftime("%d%m%M%S")
    self.arrived= time.strftime("%d/%m/%Y")
    self.adopted= None               
  
  def setAdopted(self):
    self.adopted= time.strftime("%d/%m/%Y")

  def __str__(self):
    result_str= f"{self.name}[{self.type}]"
    result_str+= f"\nArrived: {self.arrived}"
    result_str+= f"\nAdopted: {self.adopted}"
    return result_str
    
def main():
  scout= Animal("Scout", "dog")
  scout.setAdopted()
  buddy=Animal("Buddy", "cat")
  buddy.setAdopted()
  print(scout)
  print(buddy)

main()
