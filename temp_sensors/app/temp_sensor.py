import paho.mqtt.client as mqtt
import time
import os
import random

cl_name="sensors"
server="domus_server"

rooms=["bed1", "bed2", "bathroom", "living", "dining", "kitchen"]


def connectCallback(c, userdata, flags, rc):
    pass
client =mqtt.Client(cl_name)
client.on_connect=connectCallback
client.connect(server)
client.loop_start()

while True:
    print "-"*20

    rm=random.choice(rooms)
    tmp=random.randint(12,30)
    client.publish("domus/%s/temperature"%rm,"%d"%tmp)
    
    time.sleep(5)

client.loop_stop()

