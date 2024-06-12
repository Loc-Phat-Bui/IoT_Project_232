import sys
from Adafruit_IO import MQTTClient
import time
import random
# from simple_ai import *
from uart import *

AIO_FEED_IDs = ""
AIO_USERNAME = ""
AIO_KEY = ""

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_IDs:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + " feed_ID: " + feed_id)
    if feed_id == "button_1":
        if payload == "0":
            writeData("!100#")
        else:
            writeData("!101#")
    if feed_id == "button_2":
        if payload == "0":
            writeData("!200#")
        else:
            writeData("!201#")

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

counter = 10
while True:
    # counter = counter - 1
    # if counter <= 0:
    #     counter = 10

    #     print("Random data is publishing...")
    #     temp = random.randint(-6,42)
    #     client.publish("sensor_1",temp)
    #     flux = random.randint(0,600)
    #     client.publish("sensor_2",flux)
    #     humid = random.randint(0,100)
    #     client.publish("sensor_3",humid)
    # time.sleep(1)

    readSerial(client)
    pass