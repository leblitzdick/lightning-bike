##
#
# lightning-bike : An e-bike whose electrical support can be booked for a certain period of time and paid with lightning.
#
#   @filename    :   qr-invoice.py
#   @brief       :   compose and convert the qr-invoice to e-paper display matching dimensions   
#   @author      :   Matthias Steinig
#
#   Folders
#          img   :   basic Images to display   
#      testing   :   some testing stuff of course
#          tmp   :   where the composed pictures are
#
#   lbike.py main program started from /etc/rc.local 
##


import os
import subprocess
import wand
from wand.image import Image

# CONFIG
basedir = os.path.dirname(os.path.realpath(__file__))   


def callSubprocess(cmd):
      subprocess.call(cmd.split())

       
with Image(filename=basedir+'/tmp/qr.png') as qr:
      qr.transform(resize='176x264')
      qr.save(filename=basedir+'/tmp/qr.png')
      with Image(filename=basedir+'/img/pay_invoice_176x264.png') as bg:
              bg.composite(qr, 1, 1)
              bg.save(filename=basedir+'/tmp/qr_176x264.png')

      callSubprocess('convert '+basedir+'/tmp/qr_176x264.png  -type Palette -depth 2 -compress none bmp3:'+basedir+'/tmp/qr_176x264.bmp')
      


          
