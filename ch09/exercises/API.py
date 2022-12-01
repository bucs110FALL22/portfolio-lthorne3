import requests
import json

def genres():
  api_url = 'https://binaryjazz.us/wp-json/genrenator/v1/genre/'
  response= requests.get(api_url)
  genre= response.json()
  amt= 0
  if "disco" in genre:
    amt+=1
  print(amt, " genres have disco!")

genres()
