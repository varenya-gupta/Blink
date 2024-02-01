import geocoder
import geopy.geocoders

# Initialize the geolocator
geolocator = geopy.geocoders.Nominatim(user_agent="my_app")

# Get the location data of your desired location
location = geolocator.geocode(input("Please enter Location"))

# Print the latitude and longitude
print(location.longitude, location.latitude)

#get your current latitude and longitude
g = geocoder.ip('me')
print(g.latlng)
