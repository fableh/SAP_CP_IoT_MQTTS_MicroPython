# sap general configuration

SCP_IOT_PORT = 8883
SCP_IOT_HOST = '<SCP IoT Service host>'
#SCP_IOT_PATH = '/measures/f8dca15f30149def'
SCP_IOT_ROOT_CA = '/flash/cert/eu10cpiotsap.crt'
SCP_IOT_CLIENT_CERT = '/flash/cert/credential.crt'
SCP_IOT_PRIVATE_KEY = '/flash/cert/credential.key'

SCP_IOT_DEVICE='<SCP IoT Service Device ID>'
SCP_IOT_SENSOR='<SCP IoT Service Sensor ID>'
################## Capabilities #################
#Temp
SCP_IOT_CAP_TEMP="<SCP IoT Service Capability ID - TEMP>"
#Humidity
SCP_IOT_CAP_HUMIDITY="<SCP IoT Service Capability ID - HUMIDITY>"
#Battery
SCP_IOT_CAP_BATTERY="<SCP IoT Service Capability ID - BATTERY>"
#Pitch
SCP_IOT_CAP_PITCH="SCP IoT Service Capability ID - PITCH>"
#Acc
SCP_IOT_CAP_ACC="SCP IoT Service Capability ID - ACC>"
#Engine
SCP_IOT_ENGINE="SCP IoT Service Capability ID - ENGINE>"
################## Subscribe / Publish client #################
CLIENT_ID = '<SCP IoT Service Device ID>'
TOPIC_MEASURE = 'measures/<SCP IoT Service Device ID>'
TOPIC_CMD='commands/<SCP IoT Service Device ID>'
#OFFLINE_QUEUE_SIZE = -1
#DRAINING_FREQ = 2
CONN_DISCONN_TIMEOUT = 10
MQTT_OPER_TIMEOUT = 5
LAST_WILL_TOPIC = 'measures/<SCP IoT Service Device ID>'
LAST_WILL_MSG = 'To All: Last will message'
