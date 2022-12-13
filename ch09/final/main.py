import NASAapi
import GeoDataSourceAPI
import random

def main():  
  place= NASAapi.NASAapi(lon= random.randint(0, 180), lat= random.randint(0, 60))  
  city= GeoDataSourceAPI.GeoDataSourceAPI(lng=NASAapi.lon, latit=NASAapi.lat)
  p= place.get()
  
  print(f"{p.response['imagery']}, {p.response['lon']}, {p.response['lat']}")
  
  user_guess= str(input("Based on the latitude and longitude of the place in this image, what city is this?: "))
  c= city.get()
  if user_guess in c.resp['city']:
    print("correct!")
  else:
    print("nope")
    


main()