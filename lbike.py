#!/usr/bin/python
##
#
# lightning-bike : An e-bike whose electrical support can be booked for a certain period of time and paid with lightning.
#
#   @filename    :   lbike.py
#   @brief       :   Main routine
#   @author      :   Matthias Steinig
#
#   Folders
#          img   :   basic Images to display
#      testing   :   some testing stuff of course
#          tmp   :   where the composed pictures are
#
#   lbike.py main program started from /etc/rc.local
##

import epd2in7
import os
import time
import json, requests
import subprocess
import Image
import RPi.GPIO as GPIO


epd = epd2in7.EPD()
epd.init()

amount = 250000

#server IP and api token must fit your settings  
charge_url = 'http://api-token:somepassword@xxx.xxx.xxx.xxx:port'

# the 4 keys on the e-paper 2,7
key1 = 5
key2 = 6
key3 = 13
key4 = 19

# power switch relais
power = 18

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(key1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(key2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(key3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(key4, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# 255: clear the image with white
image = Image.new('1', (epd2in7.EPD_WIDTH, epd2in7.EPD_HEIGHT), 255) 
basedir = os.path.dirname(os.path.realpath(__file__))


def lightning_getInvoice(id):
      resp = requests.get(charge_url+'/invoice/'+id)
#debug
#      print(resp.json())
      return resp.json()


def lightning_createInvoice(amount, description):
      invoice_details = {"msatoshi": amount, "description": "{}".format(description) }
#debug
#      print(invoice_details)
      resp = requests.post(charge_url+'/invoice/', json=invoice_details)
#debug
#      print(resp.json())
      return resp.json()
            

def callSubprocess(cmd):
             subprocess.call(cmd.split())
             

def Invoice_paid(amount,boost_time):

    timer = 0
    invoice = lightning_createInvoice(amount, boost_time)

    callSubprocess('qrencode -s 5 -o '+basedir+'/tmp/qr.png ' + invoice['payreq'])
    callSubprocess('python '+basedir+'/show.py')

    # Wait 60s for payment 
    while timer < 60:
          print(timer)
          timer += 1
          invoice_status = lightning_getInvoice(invoice['id'])
          if invoice_status['status'] == 'paid':
                return True
          time.sleep(1)
          

# switch the time with BOOOOST
def relaisTime(int):
    GPIO.setup(power, GPIO.OUT)
    GPIO.output(power, GPIO.LOW)
    time.sleep(int)
    GPIO.output(power, GPIO.HIGH)


# display "Welcome to lightning bike" 
def displayWelcomeScreen():
    epd.display_frame(epd.get_frame_buffer( Image.open(''+basedir+'/img/welcome_176x264.bmp')))

    
# display "Enjoy your ride" 
def enjoyYourRide():
    epd.display_frame(epd.get_frame_buffer( Image.open(''+basedir+'/img/eyr_176x264.bmp')))
         


    
def main():

    welcome = True
        
    while True:
        key1state = GPIO.input(key1)
        key2state = GPIO.input(key2)
        key3state = GPIO.input(key3)
        key4state = GPIO.input(key4)

        # reduce CPU usage
        time.sleep(0.005) 

        if welcome == True:
            displayWelcomeScreen()
            welcome = False
        
        if key1state == False:
              print('Key1 Pressed')
              if Invoice_paid(amount,'1min BOOOST' ) == True:
                    enjoyYourRide()
                    relaisTime(60)
              displayWelcomeScreen()
            
        if key2state == False:
              print('Key2 Pressed')
              if Invoice_paid((amount*3),'3min BOOOST' ) == True:
                    enjoyYourRide()
                    relaisTime(180)
              displayWelcomeScreen()
            
        if key3state == False:
              print('Key3 Pressed')
              if Invoice_paid((amount*5),'5min BOOOST' ) == True:
                    enjoyYourRide()
                    relaisTime(300)
              displayWelcomeScreen()
            
        if key4state == False:
              print('Key4 Pressed')
              displayWelcomeScreen()
              welcome = False


if __name__ == '__main__':
    main()

