import folium
from geopy.geocoders import Nominatim
from IPython.display import display, HTML

# Create a map with search using python

location_name = input('Enter your location: ')

geolocator = Nominatim(user_agent="geoapi")
location = geolocator.geocode(location_name)

if location:
    #create a center map based on user request.
    latitude = location.latitude
    longitude = location.longitude
    clcoding = folium.Map(location=[latitude, longitude], zoom_start=12)
    
    marker = folium.Marker([latitude, longitude],popup=location_name)
    marker.add_to(clcoding)
    
    display(HTML(clcoding._repr_html_()))
else:
    print(f"No {location_name} : Found, please search again! ")