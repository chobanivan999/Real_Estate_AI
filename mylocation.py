import geocoder
from datetime import datetime

myloc = geocoder.ip('me')
mylocation = myloc.current_result.json
country = mylocation['country']
city = mylocation['city']
state = mylocation['state']

print(country)
print(city)
print(state)

date_object = datetime.fromtimestamp(1067932800)
print(date_object)