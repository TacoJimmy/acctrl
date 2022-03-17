
# coding:utf-8
import codecs
import json
import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connected with result code"+str(rc))
    client.subscribe('v1/devices/me/rpc/request/+',1)
    time.sleep(3)

def on_message(client, userdata, msg):
    data_topic = msg.topic
    data_payload = json.loads(msg.payload.decode())
    time.sleep(.5)
    listtopic = data_topic.split("/")  
    signal_fb = 'v1/devices/me/rpc/response/'+str(listtopic[5]) # response topic
    fb_payload = {'good': 1}
    print(data_payload)
    client.publish(signal_fb,json.dumps(fb_payload)) # send respose

def ipc_subscribe():
    meter_token = "GAruSGOZYNeLWtbGD9D5"
    meter_pass = ''
    url = 'thingsboard.cloud'

    client = mqtt.Client()
    client.on_connect = on_connect
    time.sleep(.5)
    client.on_message = on_message
    time.sleep(.5)
    
    client.username_pw_set(meter_token, meter_pass)
    client.connect(url, 1883, 60)


    client.loop_forever()

while True:
    
    ipc_subscribe()
    time.sleep(10)