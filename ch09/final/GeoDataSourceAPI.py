import requests


class GeoDataSourceAPI:
  def __init__(self, lng, latit):
    self.url= f'https://api.geodatasource.com/v2/city/key=Enter_API_Key&{lng}&{latit}'
   

  def get(self):
    '''
    gets city name information from the GeoDataSource API
    args: (object) self
    return: (str) Name of city
    '''
    p= requests.get(self.url)
    resp= p.json()

    if resp.get('city'):
      return resp['city']
    else:
      return None
