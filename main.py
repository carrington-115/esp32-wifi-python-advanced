# # main.py -- put your code here!
import network # this is the network library
from machine import Pin
from time import sleep, sleep_ms, sleep_us  # the functions are the normal sleep functions for milliseconds, microseconds

led = Pin(2, Pin.OUT)
def connect_to_wifi_STA_MODE():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connecting to the network")
        wlan.connect("AndroidAP6a34", "urjr7604")
        while not wlan.isconnected():
            blink_led(1)
            pass
    
    #finally the device should have connected
    while wlan.isconnected():
        print("I have connected to the network")
        print(f"The network configuration: {wlan.ifconfig()}")
        blink_led(2)


def blink_led(n):
    led.value(1)
    sleep(n)
    led.value(0)

def actAsAccessPoint():
    wlan = network.WLAN(network.AP_IF)
    wlan.config(ssid="ESP", password="esp32", max_clients=10)
    # wlan.config(max_clients=10)
    wlan.active(True)
    done = True
    while done:
        print("An access point has connected")
        sleep(1)
        connectedDevice = wlan.ifconfig()
        print(f"The location of the connected device is {connectedDevice}")
        blink_led()


def blink_with_ms(t):
    led = Pin(2, Pin.OUT)
    led.value(1)
    sleep_ms(t) # you can do the same for microseconds by using sleep_us()
    led.value(0)



# this is the section to run the program
while True:
    print("The code has started running this proof you are in the main program of the code\n")
    # connect_to_wifi_STA_MODE() # This was the connect in STA MOD
    # actAsAccessPoint() # this is the function that show how to make the esp32 an access point other devices can connect to
    blink_with_ms(500)
     
        

# import time
# import machine
# pin = machine.Pin(2, machine.Pin.OUT)
# while True:
#     pin.value(1)
#     time.sleep(2)
#     pin.value(0)    