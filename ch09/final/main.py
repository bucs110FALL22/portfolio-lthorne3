import NASAapi
import GeoDataSourceAPI
import random

def main():  
  place= NASAapi.NASAapi(longitude= random.randint(0, 180), latitude= random.randint(0, 60))
  p= place.get()
  city= GeoDataSourceAPI.GeoDataSourceAPI(longitude=98, latitude=60)
  c=city.get()
  

main()