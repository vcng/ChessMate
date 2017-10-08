// This is the LED Hardware Library 
// for use with the ChessMate Project

// Header File
#ifndef LED_H
#define LED_H

#include "Arduino.h"
#include "Adafruit_NeoPixel.h"

#define PIN 6

#define NUM_LEDS 8

#define BRIGHTNESS 5

class Led {
    private:
        int led_array[8][8] = 
        {
            {0, 1 ,2 ,3 ,4 ,5 ,6 , 7},
            {15,14,13,12,11,10, 9, 8},
            {16,17,18,19,20,21,22,23},
            {31,30,29,28,27,26,25,24},
            {32,33,34,35,36,37,38,39},
            {47,46,45,44,43,42,41,40},
            {48,49,50,51,52,53,54,55},
            {63,62,61,60,59,58,57,56}
        };

        Adafruit_NeoPixel strip;
    
    public:

        void startStrip();
        
        /*
        This function is going to be used to show the possible movements
        when the piece is lifted up given from the XOR function that is
        defined in the Integrate library. This will show the exact location
        on where to light up that LED based on that coordinate.
        */
        void showMove(char x, char y);



        void hideMove(char x, char y);

        /*
        This function just pushes all the updated coordinates
        to the bard to light up the LED's.
        */
        void update();




    };

#endif