##
#
# lightning-bike : An e-bike whose electrical support can be booked for a certain period of time and paid with lightning.
#
#   @filename    :   show.py  
#   @brief       :   create the qr code from the invoice and show it on the Display
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
import Image
import subprocess
import os

# CONFIG
basedir = os.path.dirname(os.path.realpath(__file__))

def callSubprocess(cmd):
    subprocess.call(cmd.split())
           

def main():
    epd = epd2in7.EPD()
    epd.init()


    callSubprocess('python '+basedir+'/qr-invoice.py')

    # display QR code
    epd.display_frame(epd.get_frame_buffer(Image.open(''+basedir+'/tmp/qr_176x264.bmp')))

if __name__ == '__main__':
    main()
