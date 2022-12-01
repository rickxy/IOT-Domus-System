#!/usr/bin/python
import paho.mqtt.client as mqtt
import time, datetime
logFile="/var/www/html/cpanel/status.txt"
cl_name="watchdog"
server="127.0.0.1"
statuslog=[]
errorlog=[]

class StringAccumulator(object):
    def __init__(self):
        self.s=""
    def append(self,s):
        self.s+=s
        self.s+="\n"
    def __str__(self):
        return self.s

def connectCallback(c, userdata, flags, rc):
    print "Connection result:",rc
    if rc==0:
        c.publish("domus/meta/status/colonel","OK")
    else:
        c.publish("domus/meta/status/colonel","ERROR")
def msgCallback(c, userdata, message):
    print "Got a message"
    topicParts=message.topic.split("/")
    err=False
    print message.topic
    if len(topicParts)==4:
        if topicParts[0]=="domus" and topicParts[1]=="meta":
            if topicParts[2]=="status":
                service=topicParts[3]
                if message.payload in ["OK", "ERROR", "STARTUP","SHUTDOWN","ON","OFF"]:
                    statuslog.append((datetime.datetime.now(),"Status of %s is %s"%(service,message.payload)))
		if message.payload in ["Fake__sensor", "Extra_sensor",]:
                    statuslog.append((datetime.datetime.now(),"Status of %s is %s"%(service,message.payload)))
                else:
                    statuslog.append((datetime.datetime.now(),"Recieved invalid status update from %s"%service))
            else:
                err=True
    elif len(topicParts)==5 and topicParts[2]=="status" and topicParts[4]=="message":
        service=topicParts[3]
            
        statuslog.append((datetime.datetime.now(),"Message from %s: %s"%(service,message.payload)))
    else:
        err=True
    if err:
        statuslog.append((datetime.datetime.now(),"Recieved message (%s) for unexpected meta topic (%s)"%(message.payload, message.topic)))

client =mqtt.Client(cl_name, userdata=None)
client.on_connect=connectCallback
connected=False
while not connected:
    try:
        client.connect(server)
        connected=True
    except:
        print "Waiting on DOMUS MQTT server..."
        time.sleep(0.5)
client.subscribe("domus/meta/#")
client.on_message=msgCallback
client.loop_start()

while True:
    out=StringAccumulator()

    for i in statuslog:
        out.append("<p>%s: %s here_ </p>"%(i[0].isoformat(),i[1]))
    print out
    f=open(logFile,"w")
    f.write(str(out))
    f.close()
    time.sleep(3)
client.loop_stop()

