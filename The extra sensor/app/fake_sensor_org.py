import paho.mqtt.client as mqtt
import time, datetime
import os
import random
cl_name="fake_sensor"
server="174.19.0.40"#"domus_server"
rooms=["EC-0", "EC-1", "EC-2", "EC-3", "EC-4", "EC-4"]				
def connectCallback(c, userdata, flags, rc):
    pass
client =mqtt.Client(cl_name)
client.on_connect=connectCallback
client.connect(server)
client.loop_start()      
st_name=input("Enter your name and ID: ")
print st_name;
while True:
    print "-"*20
    print datetime.datetime.now()
    print st_name
    rm=random.choice(rooms)
    nop=random.randint(10,100)
    print "There are ",nop,"FAKE people in room ",rm 
    client.connect(server)
    client.publish("Fake__sensor/%s/detected "%nop,"%s"%rm)
    
    time.sleep(5)

client.loop_stop()