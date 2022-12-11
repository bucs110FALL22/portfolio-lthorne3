import requests
import random

class NASAapi:
  def __init__(self, longitude= random.randint(0, 180), latitude= random.randint(0, 60)):
    self.url= f'https://api.nasa.gov/planetary/earth/imagery?{longitude}&{latitude}&date=2022-12-01&api_key=DEMO_KEY'

   

  def get(self):
    r= requests.get(self.url)
    response= r.json()
    print(response)

  def changeImage(self, image):
    pass

