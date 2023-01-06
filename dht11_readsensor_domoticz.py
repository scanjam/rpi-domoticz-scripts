import sys
import board
import adafruit_dht
import urllib.request

# parameters
#DHT_type    = 11
#OneWire_pin = 4
sensor_idx  = 1
url_json    = "http://192.168.0.15:8080/json.htm?type=command&param=udevice&idx="
#verbose     = 1  # set to 1 to print out information to the console 

# read dht11 temperature and humidity
#humidity, temperature = adafruit_dht.read_retry(DHT_type, OneWire_pin)
dht = adafruit_dht.DHT11(board.D4, use_pulseio=False)
temperature = dht.temperature
humidity = dht.humidity

# use Domoticz JSON url to update
cmd = url_json  + str(sensor_idx) + "&nvalue=0&svalue=" + str(temperature) + ";" + str(humidity) + ";0"
hf = urllib.request.urlopen(cmd)
#if verbose > 0:
#  print 'Sensor data: temperature = {0:0.1f}C,  humidity =  {1:0.1f}%'.format(temperature, humidity)
#  print 'Uploaded to Pi: ' + cmd
#  print 'Response: ' + hf.read()
# hf.close
