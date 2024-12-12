# FrSkyPixelOSD
FrSkyPixelOSD is a pixel-based OSD product launched by FrSky.
It allows users to set the content and location of the OSD based on graphics.The protocol & API interface definition are public to whom
may want to develop on it.

## OSD Modules
At present, there are two kinds of products: independent OSD module for average user and OSDMini for FC factory.
It can totally replace the MAX7456 solution and bring graphic features.

Up to now, iNav,Betaflight,ArduPilot are all working on supporting on it.


### Standalone OSD module
#### Specifications:
* Size:              19x18x3 (LxWxH in mm)
* Current:           38mA @ 5V
* Operating Voltage: 5v
* Weight：           1.5g

#### Interface
* +5v：      VCC 5V
* VID_GND:   Video GND
* VID_IN:    Video Input
* VID_OUT:   Video Output
* RX/TX:     USART to Flight Controller

### OSDMini for Flight controller factories
#### Specifications:
* Size:              7x7x2 (LxWxH in mm)
* Current:           20mA @ 3.3V
* Operating Voltage: 3.3v
* Weight：           0.3g

#### Interface
* 3.3v：   VCC 3.3V
* GND:     GND
* RX/TX:   USART to Flight Controller
* VI:      Video Input
* VO:      Video Output
* D/C/G:   Program Port


FrSky Pixel OSD Python SDK
==========================

This Python SDK can be used to quickly prototype drawing code that
interacts with the OSD.

The `frkskyosd.py` file can also be directly invoked as a Python
program for performing several tasks like font uploading and
firmware updates. It can also connect to both real devices (passing
the path to the port) or to the OSD simulator (passing host:port).
Invoke it without any arguments to see its help.

SDK functions are named after their remote API functions and are
roughly equivalent. Please, see the main documentation for an
explanation of what each function does.