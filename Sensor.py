#!/usr/bin/env python2.7

import Adafruit_BBIO.ADC as ADC
import time

sensor = "P9_40"
ADC.setup(sensor)
while True:
        out = ADC.read(sensor)
        data = out * 1800
        cel = data /10
#cel = data/22.75
        print(cel)
        time.sleep(5)

