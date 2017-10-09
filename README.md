# ChessMate
ChessMate is here to provide new chess players a more interactive learning experience.

## Setting up and using the MVP

After grabbing the release, you can try out the MVP with the following steps:

> Note: You need our custom-made **ChessMate Board** to use this software.

### 1. Install Python 2.7 on the controller

The controller is typically a `Raspberry Pi`. Raspbian Linux comes with this installed.
If **Python 2.7** is not already installed, you can install it from the [python website](https://www.python.org/downloads/).

### 2. Flash the arduino firmware

Using `Arduino Studio`, ensure the following libraries are loaded:
- Adafruit NeoPixel. More info on installing libraries: [Arduino Libraries](https://www.arduino.cc/en/Guide/Libraries)

Flash the device with the `.ino` file by opening the `.ino` file in `Arduino Studio`. Select the port that the `Arduino` is on and select the `Arduino Mega` for a device.

### 3. Plug in the power to the board and arduino

### 4. Plug in the power to the controller (Most likely the pi)

### 5. Begin playing