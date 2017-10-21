// This is the LED Hardware Library 
// for use with the ChessMate Project

// Header File
#ifndef LED_H
#define LED_H

#include "Arduino.h"
#include "Adafruit_NeoPixel.h"
#include "protocol.h"


#define PIN 52

#define NUM_LEDS 64

#define BRIGHTNESS 255


/*     Starts the strip     */
void led_init();


/*  This function is going to be used to show the possible movements
when the piece is lifted up given from the XOR function that is
defined in the Integrate library. This will show the exact location
on where to light up that LED based on that coordinate. */
void led_show_move(char color, char x, char y);


/*   This function will just hide a move at the coordinates given    */
void led_hide_move(char x, char y);


/*  This function just pushes all the updated coordinates
to the bard to light up the LED's.  */
void led_update();


#endif