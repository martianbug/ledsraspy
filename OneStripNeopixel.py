#include all neccessary packages to get LEDs to work with Raspberry Pi
import time
import board
import neopixel

#Initialise a strips variable, provide the GPIO Data Pin
#utilised and the amount of LED Nodes on strip and brightness (0 to 1 value)
pixels = neopixel.NeoPixel(board.D18, 30,bpp=4, brightness=1)

#Also create an arbitary count variable
x=0

#Focusing on a particular strip, use the command Fill to make it all a single colour
#based on decimal code R, G, B. Number can be anything from 255 - 0. Use a RGB Colour
#Code Chart Website to quickly identify a desired fill colour.
print("Filling red")
pixels.fill((255, 0, 0))
pixels.show()
#Below demonstrates how to individual address a colour to a LED Node, in this case
#LED Node 10 and colour Blue was selected
pixels[10] = (0, 20, 255)

#Sleep for three seconds, You should now have all LEDs showing light with the first node
#Showing a different colour
time.sleep(10)

#Little Light slider script, it will produce a nice loading bar effect all the way up
#and then all the way back
#This was created using a While Loop taking advantage of that arbitary variable to determine
#which LED Node we will taget/index with a different colour

#Below will loop until variabe x has value 35
while x<30:
    pixels[x] = (255, 0, 0)
    pixels[x-5] = (255, 0, 100)
    pixels[x-10] = (0, 0, 255)
    #Add 1 to the counter
    x=x+1
    #Add a small time pause which will translate to 'smoothly' changing colour
    time.sleep(0.05)

#below section is the same process as above loop just in reverse
while x>-15:
    pixels[x] = (255, 0, 0)
    pixels[x+5] = (255, 0, 100)
    pixels[x+10] = (0, 255, 0)
    x=x-1
    time.sleep(0.05)

#Add a brief time delay to appreciate what has happened    
time.sleep(4)

#Complete the script by returning all the LED to off
pixels.fill((0, 0, 0))

print('Program finished!')
