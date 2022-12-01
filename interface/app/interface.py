#!/usr/bin/python
import paho.mqtt.client as mqtt
import time, datetime
from alchemy import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
#Accepts
# - domus/interface/command/refresh
#    causes database to be requeried and causes the interface to publish current status
# - domus/interface/command/interval (1 to 20)
#   - changes the updateinterval - seconds between updating heating system

#Publishes
# - domus/interface/status/interval
#   On any change to interval, the new value is published

interval=5
engine = None
Session = None

cl_name="interface"
server="domus_server"



pw=None

def connectCallback(c, userdata, flags, rc):
    global engine
    global Session
    # client
    #     the client instance for this callback
    # userdata
    #     the private user data as set in Client() or userdata_set()
    # flags
    #     response flags sent by the broker
    # rc
    #     the connection result: 0: Connection successful 1:
    #     Connection refused - incorrect protocol version 2:
    #     Connection refused - invalid client identifier 3: Connection
    #     refused - server unavailable 4: Connection refused - bad
    #     username or password 5: Connection refused - not authorised
    #     6-255: Currently unused.


    print "Connection result:",rc
    if rc==0:
        c.publish("domus/meta/status/interface","STARTUP")
        engine = create_engine('mysql+mysqldb://domus:carpetseller@domus_db/domus', echo=False)
        Session = sessionmaker(bind=engine)

    else:
        c.publish("domus/meta/status/interface","ERROR")

def msgCallback(c, userdata, message):
    global volume
    topicParts=message.topic.split("/")
    err=False
    print message.topic,message.payload
    if len(topicParts)==3 and topicParts[2]=="command":
        pieces=message.payload.split("/")
        if len(pieces)!=2 or pieces[0]!=pw: 
            c.publish("domus/meta/status/interface/message", "Command not given with preceding password, such as 'pass/birghtness', or password incorrect.")
        else:
            c.publish("domus/meta/status/interface/message", "Currently only interval commands supported. Send pass/34 (for example) on domus/interface/command/interval")
        #PROCESS MESSAGE
    elif len(topicParts)==4 and topicParts[2]=="command" and topicParts[3]=="interval":
        pieces=message.payload.split("/")
        if len(pieces)!=2 or pieces[0]!=pw: #userdata contains the password
            c.publish("domus/meta/status/interface/message", "Interval not given with preceding password, such as 'pass/30' or password incorrect.")
            print pw
            print pieces[0]
        else:
            interval=eval(pieces[1])
            try:
                if 0<interval<=20:
                    
                    c.publish("domus/meta/status/interface/message", "interval set to %d"%int(interval))
                    c.publish("domus/interface/status/interval", "%d"%int(interval))
                else:
                    c.publish("domus/meta/status/interval/message", "Values for interval must lie between 1 and 20 inclusive")
            except:
                print "Error sending message. Possibly a value that can't be processed with eval()."
    else:
        err=True
    if err:
        c.publish("domus/meta/status/interval/message", "Recieved unexpected message (%s) or unexpected topic (%s)"%(message.payload, message.topic))





client =mqtt.Client(cl_name, userdata=None)
client.on_connect=connectCallback
client.connect(server)
client.subscribe("domus/interface/#")
client.on_message=msgCallback
client.loop_start()

ready=False


while True:

    if not ready:
        print "Interface starting up..."
    if Session!=None and ready==False:
        session=Session()
        if pw==None:
            #Get user password from database
            pw=session.query(HomeSetting).filter(HomeSetting.param=="interface_password").one().value



        ready=True
        client.publish("domus/meta/status/interface","OK")
        client.publish("domus/meta/status/interface/message", "Currently only interval commands supported. Send pass/34 (for example) on domus/interface/command/interval")
    else:
        print "Interface ready"    
    time.sleep(3)
client.loop_stop()

