#The below code runs on Python 2
#You must be connected to the internet for the application to work
import urllib2
import json
#Connection to the API
f = urllib2.urlopen('http://api.wunderground.com/api/3ac6e1e077040844/geolookup/conditions/forecast/q/Australia/Sydney.json')
json_string = f.read()

parsed_json = json.loads(json_string)

#Variables are assigned the fetched data
location = parsed_json['location']['city']

temp_f = parsed_json['current_observation']['temperature_string']

gps_lon=parsed_json['location']['lat']

gps_lat=parsed_json['location']['lon']

humid=parsed_json['current_observation']['relative_humidity']

wind=parsed_json['current_observation']['wind_mph']

#The data is printed via a the CMD
print "\n"
print "===================================================================="
print "The current temperature in %s is: %s" % (location, temp_f)
print "\n"
print "The GPS cordinates for %s are %s %s" % (location,gps_lat, gps_lon)
print "\n"
print "The current relative humidity is: %s" % (humid)
print "\n"
print "The current wind speed in MPH is: %s" % (wind)
print "\n"
print "===================================================================="
print "HOPE YOU HAVE ENJOYED GETTING WEATHER UPDATES FROM SYDNEY !"
print "\n"

f.close()