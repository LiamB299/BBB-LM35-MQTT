#!/usr/bin/env python2.7

import datetime
import paho.mqtt.client as mqtt
import random as rnum
import time as sl
import Adafruit_BBIO.ADC as ADC

#broker = "m24.cloudmqtt.com"
#user = "zobxixxh"
#password = "7tWaXx229B7D"
#port = 19817

broker = "192.168.21.64"
port = 1883

def temp_retrieve():
        ADC.setup("P9_40")
        read = ADC.read("P9_40")
        return (read * 180)

def on_connect(client, userdata, flags, rc):
        print("Connection Established")

def on_log(client, userdata, level, buf):
        print("Log: ", buf)

def on_disconnect(client, userdata, rc):
        print("Disconnected from server. Check Network Connection.")
        client.reconnect()

def on_publish(client, userdata, mid):
        print("Message sent successfully")

def main():
        client = mqtt.Client("BBB", False)
        #client.username_pw_set(user,password)
        client.connect_async(broker,port,60)
        client.on_connect=on_connect
        client.loop_start()
        ADC.setup()
        client.max_inflight_messages_set(30)
        while True:
                num = temp_retrieve() #rnum.randint(20,34)
                date = datetime.datetime.now().strftime("%d/%m/%Y")
                time = datetime.datetime.now().strftime("%H:%S")
                upload = str(num)+"&"+time+"&"+date
                client.publish("TestLiam", upload, 1)
                sl.sleep(5)
                client.on_log=on_log
                client.on_disconnect=on_disconnect
                client.on_publish=on_publish
        client.loop_stop()
        return 0;

main() 


