import paho.mqtt.client as mqtt
import time,base64
import datetime
from alchemy import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import urllib2
import random

cl_name="fake_sensor"
server="174.19.0.40"#"domus_server"

rooms=["EC-0", "EC-1", "EC-2", "EC-3", "EC-4", "EC-4"]

engine = None
Session = None
tTemp = None
interval=[5]
def connectCallback(c, userdata, flags, rc):
    global engine
    global Session
    if rc==0:
        c.publish("domus/meta/status/fake_sensor","STARTUP")
        engine = create_engine('mysql+mysqldb://domus:carpetseller@domus_db/domus', echo=False)
        Session = sessionmaker(bind=engine)

    else:
        c.publish("domus/meta/status/fake_sensor","ERROR")

def msgCallback(c, userdata, message):
    topicParts=message.topic.split("/")
    houseTemps[topicParts[1]]=float(message.payload)

st_name=input("Enter your name and ID: ")
print st_name;

client =mqtt.Client(cl_name)
client.on_connect=connectCallback
print server
client.connect(server)
client.loop_start()

ready=False
count=0
while True:
    print "-"*20
    if Session!=None and ready==False:
        session=Session()
        if tTemp==None:
            client.publish("domus/meta/status/fake_sensor","OKOKOKOK")
            ready=True
    if ready:
        print datetime.datetime.now()
        print st_name
        rm=random.choice(rooms)
        nop=random.randint(10,100)
        print "There are ",nop,"FAKE people in room ",rm 
	out = "Fake__sensor/%s/detected "%nop,"%s"%rm
        client.publish("domus/meta/status/fake_sensor","Fake__sensor/%s/detected "%nop,"%s"%rm)
    
        time.sleep(5)


    #count=(count+1)%30
    #print("Sleeping for %d seconds"%interval[0])
    #time.sleep(interval[0])

client.loop_stop()

