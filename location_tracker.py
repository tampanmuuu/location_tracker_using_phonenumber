import phonenumbers
import opencage
import folium
number = "+6288704564348"
from phonenumbers import geocoder
pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import OpenCageGeocode
key = 'd654c8039f834cf9abb4efac2c3ca1f6'
geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

my_map = folium.Map(location = [lat,lng], zoom_start = 9)
folium.Marker([lat,lng], popup=location).add_to(my_map)

my_map.save("mylocation.html")

