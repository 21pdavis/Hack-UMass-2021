#!/usr/bin/python

import picamera import PiCamera as pc
import numpy as np
import cv2
from time import sleep

class PeopleSensor:
    def __init__(self):
        # bool for determining status of camera
        self.capturing = False

        self.camera = PiCamera()
        self.camera.resolution(800, 480)
        #camera.vflip = True <-- if need to fix the image
        # self.camera.start_preview()
        # camera warm-up time
        sleep(2)
        self.run()

    def run(self):
        while True:
            self.camera.capture("current_image.jpg")
            sleep(0.5) # arbitrary, can be adjusted
            self.analyze("current_image.jpg")

    def analyze(self, file_name):
        pass
        # code to analyze image
