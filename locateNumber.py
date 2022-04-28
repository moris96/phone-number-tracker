import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from opencage.geocoder import OpenCageGeocode

number = input('Enter a mobile number with country code: ')
number = phonenumbers.parse(number)

#geocoder API key for lat & lon coordinates
key = '{insert your API Key here}'


#US state where the number is from, or province and etc for non-US countries
country_location = geocoder.description_for_number(number, "en")
print(country_location)

#timezone
print(timezone.time_zones_for_number(number))

#carrier
print(carrier.name_for_number(number, "en"))

#making sure it's a valid number
print("Valid movile number: ", phonenumbers.is_valid_number(number))


#lat & lon coordinates for number
geocoder = OpenCageGeocode(key)

query = str(country_location)

results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lon = results[0]['geometry']['lng']
print(lat, lon)
