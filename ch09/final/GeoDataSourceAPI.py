import requests


class GeoDataSourceAPI:
  def __init__(self, longitude, latitude):
    self.url= f'https://api.geodatasource.com/v2/city/key=Enter_API_Key&{longitude}&{latitude}'
   

  def get(self):
    r= requests.get(self.url)
    resp= r.json()
    print(resp)
