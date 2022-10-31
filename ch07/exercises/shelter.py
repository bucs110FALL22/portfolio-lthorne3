import time

class Animal:
  def __init__ (self, name, animal):
    self.name= name
    self.animal= animal
    self.date= date
  
  def getName(self):
    return self.name

  def getAnimal(self):
    return self.animal

  def getId(self):
    return id(self)

  def setAdopted(self):
    return true

  def getDate(self):
    return date(self)
  

    
  def main():
    scout= Animal("Scout", "dog", 1234)
    scout.setAdopted()
    print(id(scout))

  main()
