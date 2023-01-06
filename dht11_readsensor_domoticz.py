import sys
import board
import adafruit_dht
import urllib.request

# parameters
sensor_idx  = 1
url_json    = "http://192.168.0.15:8080/json.htm?type=command&param=udevice&idx="
dht = adafruit_dht.DHT11(board.D4, use_pulseio=False)
temperature = dht.temperature
humidity = dht.humidity
# use Domoticz JSON url to update
cmd = url_json  + str(sensor_idx) + "&nvalue=0&svalue=" + str(temperature) + ";" + str(humidity) + ";0"
hf = urllib.request.urlopen(cmd)

