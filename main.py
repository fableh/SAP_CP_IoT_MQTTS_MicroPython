from pysense import Pysense
from LIS2HH12 import LIS2HH12
from SI7006A20 import SI7006A20
from LTR329ALS01 import LTR329ALS01
from MPL3115A2 import MPL3115A2,ALTITUDE,PRESSURE
from MQTTLib import AWSIoTMQTTClient
import config
import time

py = Pysense()
#mp = MPL3115A2(py,mode=ALTITUDE) # Returns height in meters. Mode may also be set to PRESSURE, returning a value in Pascals
si = SI7006A20(py)
lt = LTR329ALS01(py)
li = LIS2HH12(py)

def getTemperature():
	temp = "[[" +str(si.temperature())+"]]"
	print("Temp" + temp)
	return temp

def getHumidity():
	hum = "[["+str(si.humidity())+"]]"
	print("hum" + hum)
	return hum

def getBatteryVoltage():
	battery="[["+str(py.read_battery_voltage())+"]]"
	print("battery" + battery)
	return battery

def getRoll():
	roll="[["+str(li.roll())+"]]"
	print("roll" + roll)
	return roll

def getPitch():
	pitch="[["+str(li.pitch())+"]]"
	print("pitch" + pitch)
	return pitch

def getAcc():
	acc = li.acceleration()
	acc="[["+ str(acc[0]) + "," + str(acc[1]) + "," + str(acc[2]) + "]]"
	print("acc" + acc)
	return acc

def getLight():
	light = lt.light()
	light="[["+str(light[0])+ "," + str(light[1])+ "]]"
	print("BlueLux/RedLux" + light)
	return light

def getEngine():

	engine = "[[" "\"LIEBHERR RT 936\"" "," +str(si.temperature())+ "," +str(si.humidity())+ "]]"
	print("Engine Data" + engine)
	return engine


def customCallback(client, userdata, message):
	print("Received a new message: ")
	print(message.payload)
	print("from topic: ")
	print(message.topic)
	print("--------------\n\n")


# configure the MQTT client
pycomAwsMQTTClient = AWSIoTMQTTClient('<SCP IoT Service Device ID>')
pycomAwsMQTTClient.configureEndpoint(SCP_IOT_HOST, SCP_IOT_PORT)
pycomAwsMQTTClient.configureCredentials(SCP_IOT_ROOT_CA, SCP_IOT_PRIVATE_KEY, SCP_IOT_CLIENT_CERT)
pycomAwsMQTTClient.configureConnectDisconnectTimeout(config.CONN_DISCONN_TIMEOUT)
pycomAwsMQTTClient.configureMQTTOperationTimeout(config.MQTT_OPER_TIMEOUT)

if pycomAwsMQTTClient.connect():
    print('SAP CP IoT Service connection succeeded')

# Subscribe to topic
pycomAwsMQTTClient.subscribe(config.TOPIC_CMD, 1, customCallback)
time.sleep(2)


while(True):
	#payload_engine = "{ \"capabilityAlternateId\": \""+config.SCP_IOT_ENGINE+"\",\"sensorAlternateId\": \""+config.SCP_IOT_SENSOR+"\", \"measures\":\"PySense_LoPy4_01\",si.humidity()"\",\""si.humidity()"\"}"
	payload_engine = "{ \"capabilityAlternateId\": \""+config.SCP_IOT_ENGINE+"\",\"sensorAlternateId\": \""+config.SCP_IOT_SENSOR+"\", \"measures\":"+getEngine()+"}"
	result=pycomAwsMQTTClient.publish(config.TOPIC_MEASURE, payload_engine, 1)
	print(payload_engine)
	payload_acc = "{ \"capabilityAlternateId\": \""+config.SCP_IOT_CAP_ACC+"\",\"sensorAlternateId\": \""+config.SCP_IOT_SENSOR+"\", \"measures\":"+getAcc()+"}"
	result=pycomAwsMQTTClient.publish(config.TOPIC_MEASURE, payload_acc, 1)
	payload_temp = "{ \"capabilityAlternateId\": \""+config.SCP_IOT_CAP_TEMP+"\",\"sensorAlternateId\": \""+config.SCP_IOT_SENSOR+"\", \"measures\":"+getTemperature()+"}"
	result=pycomAwsMQTTClient.publish(config.TOPIC_MEASURE, payload_temp, 1)
	payload_hum = "{ \"capabilityAlternateId\": \""+config.SCP_IOT_CAP_HUMIDITY+"\",\"sensorAlternateId\": \""+config.SCP_IOT_SENSOR+"\", \"measures\":"+getHumidity()+"}"
	result=pycomAwsMQTTClient.publish(config.TOPIC_MEASURE, payload_hum, 1)
	time.sleep(5)
	payload_battery = "{ \"capabilityAlternateId\": \""+config.SCP_IOT_CAP_BATTERY+"\",\"sensorAlternateId\": \""+config.SCP_IOT_SENSOR+"\", \"measures\":"+getBatteryVoltage()+"}"
	result=pycomAwsMQTTClient.publish(config.TOPIC_MEASURE, payload_battery, 1)
	payload_acc = "{ \"capabilityAlternateId\": \""+config.SCP_IOT_CAP_ACC+"\",\"sensorAlternateId\": \""+config.SCP_IOT_SENSOR+"\", \"measures\":"+getAcc()+"}"
	result=pycomAwsMQTTClient.publish(config.TOPIC_MEASURE, payload_acc, 1)
	time.sleep(5)
	payload_acc = "{ \"capabilityAlternateId\": \""+config.SCP_IOT_CAP_ACC+"\",\"sensorAlternateId\": \""+config.SCP_IOT_SENSOR+"\", \"measures\":"+getAcc()+"}"
	result=pycomAwsMQTTClient.publish(config.TOPIC_MEASURE, payload_acc, 1)
	payload_pitch = "{ \"capabilityAlternateId\": \""+config.SCP_IOT_CAP_PITCH+"\",\"sensorAlternateId\": \""+config.SCP_IOT_SENSOR+"\", \"measures\":"+getPitch()+"}"
	result=pycomAwsMQTTClient.publish(config.TOPIC_MEASURE, payload_pitch, 1)
	time.sleep(5)
