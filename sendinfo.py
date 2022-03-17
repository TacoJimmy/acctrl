import paho.mqtt.client as mqtt
import json  
import time
import ACCtrl

def on_publish():
    AC_Status = ACCtrl.AC_ReadFullFunction('/dev/ttyS1',15)
    print(AC_Status)
    if (AC_Status[5] == 1):
        print('send data')
        client = mqtt.Client()
        client.username_pw_set("GAruSGOZYNeLWtbGD9D5","xxxx")
        client.connect('thingsboard.cloud', 1883, 60)
        payload = {'airconditiongstatus' : AC_Status[0],'operationmode' : AC_Status[1],'windspeed' : AC_Status[2],'settemperature' : AC_Status[3], 'roomtemperature' : AC_Status[4]  }
        print (json.dumps(payload))
        client.publish("v1/devices/me/telemetry", json.dumps(payload))
        time.sleep(1)
        


while True:
    
    on_publish()

    time.sleep(10)