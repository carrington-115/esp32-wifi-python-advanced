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

# this function is a function that shows all the functions available in the pin
def pin_functions():
    # creating a pin in the program
    pin = Pin(2, Pin.OUT) # Using Pin this way because I destructure it on calling machine at the top of the program.and
    pin.on() # the on() function can be used to set the pin high

    pin.off() # the off() can be used to set the pin low    

def blinK_sketch_with_abstract_functions():
    # pin = Pin(2, Pin.OUT)
    # we can still using the pin.value(1 or 0) in the program to set the value of the pin
    # if the pin is suppose to be in input, Pin(2, Pin.IN) and one can further set the pin in either pull up or pull down Pin(2, Pin.IN, Pin.PULL_UP)
    pin = Pin(2, Pin.OUT, value=1) # on creating the pin, it is possible to set the value of the pin. e.g. the value here has been set to 1 that is equivalent to high
    pin.on()
    sleep_ms(2000)
    pin.off()

# this is the section to run the program
while True:
    print("The code has started running this proof you are in the main program of the code\n")
    # connect_to_wifi_STA_MODE() # This was the connect in STA MOD
    # actAsAccessPoint() # this is the function that show how to make the esp32 an access point other devices can connect to
    # blink_with_ms(500) # this test was a test for blink the led in ms
    # blinK_sketch_with_abstract_functions() # this is the sketch that test the pin abstract function of the machine library.and


