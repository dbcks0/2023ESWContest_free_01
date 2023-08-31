import os
import paho.mqtt.client as mqtt
from baby_cry_detection.prediction_simulation import prediction_simulation

import pyaudio
import numpy as np
import time
import wave
import threading
from pyfirmata import Arduino
import pyfirmata
from matplotlib import pyplot as plt
from matplotlib import animation

board = Arduino("/dev/ttyACM0")
print("Comunication Successfully started")
it = pyfirmata.util.Iterator(board)
it.start()
sensor = board.get_pin('a:0:i')
address = "192.168.1.107"

while(True) :
    sensor_value = sensor.read() # 0 ~ 1.0
    print(sensor_value)
    if sensor_value == None :
        print("None")
    elif sensor_value >= 0.8 :
        print("poob")
        mqttc = mqtt.Client("client2")
        mqttc.connect(address, 1883)
        mqttc.publish("poob", "1")
    elif sensor_value >= 0.6 :
        print("poob")
        mqttc = mqtt.Client("client2")
        mqttc.connect(address, 1883)
        mqttc.publish("poob", "2")
    elif sensor_value >= 0.4 :
        print("poob")
        mqttc = mqtt.Client("client2")
        mqttc.connect(address, 1883)
        mqttc.publish("poob", "3")
    elif sensor_value >= 0.2 :
        print("poob")
        mqttc = mqtt.Client("client2")
        mqttc.connect(address, 1883)
        mqttc.publish("poob", "4")
    else :
        print("no poob")
        mqttc = mqtt.Client("client2")
        mqttc.connect(address, 1883)
        mqttc.publish("poob", "5")
   
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
       
   
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    temp_data = int(np.average(np.abs(data)))
    #print(temp_data)
   
    stream.stop_stream()
    stream.close()
    p.terminate()
    if(temp_data > 500) :
        print("record")
        os.system('arecord -d 9 -f S16_LE -c1 -r44100 -t wav /home/user/Downloads/baby_cry_detection-master/output.wav')
        prediction_simulation.main()  
    else :
        print("no record")
    #os.system('arecord -f S16_LE -d 8 -r 44100 output.wav')