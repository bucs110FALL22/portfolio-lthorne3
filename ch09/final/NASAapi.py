import requests
import random

class NASAapi:
  def __init__(self, lon= random.randint(0, 180), lat= random.randint(0, 60)):
    self.url= f'https://api.nasa.gov/planetary/earth/imagery?lon={lon}&lat={lat}&date=2022-12-01&api_key=DEMO_KEY'

   

  def get(self):
    '''
    gets information such as the image and the latitude and longitude coordinates from the NASA API
    args: (object) self
    return: (img) NASA satellite image, (int) latitude, and (int) longitude
    '''
    r= requests.get(self.url)
    response= r.json()
    
    if response.get('imagery'):
      return response['imagery']
    else:
      return None
      
    if response.get('lon', 'lat'):
      return response['lon', 'latit']
    else:
      return None




  
