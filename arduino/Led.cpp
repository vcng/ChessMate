// This is the Led Hardware Library 
// for use with the ChessMate Project

// Source File

#include "Arduino.h"
#include "led.h"
#include "protocol.h"

//////////////////////////////////////////
//		  PRE-DEFINED VARIABLES			//
//////////////////////////////////////////
int led_array[8][8] = 
{
    {0 ,1 ,2 ,3 ,4 ,5 ,6 ,7 },
    {15,14,13,12,11,10,9 ,8 },
    {16,17,18,19,20,21,22,23},
    {31,30,29,28,27,26,25,24},
    {32,33,34,35,36,37,38,39},
    {47,46,45,44,43,42,41,40},
    {48,49,50,51,52,53,54,55},
    {63,62,61,60,59,58,57,56}
};

// DO NOT MOVE THIS INITIALIZATION
// IT WILL BREAK EVERYTHING
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUM_LEDS, PIN, NEO_GRBW + NEO_KHZ800);

//////////////////////////////////////////
//////////////////////////////////////////
//////////////////////////////////////////

// startStrip defintion
void led_init() {
    pinMode(PIN, OUTPUT);
    strip.begin();
    strip.show();
}

// showMove definition
void led_show_move(char color, char x, char y) {
    int r = x - '0'; // convert ASCII
    int c = y - '0'; // convert ASCII

    switch(color){
        case 'w': 
            strip.setPixelColor(led_array[r][c], strip.Color(255, 255, 255, 0));
            break;
        case 'g':
            strip.setPixelColor(led_array[r][c], strip.Color(0, 255, 0, 0));
            break;
        case 'r':
            strip.setPixelColor(led_array[r][c], strip.Color(255, 0, 0, 0));
            break;
        case 'b':
            strip.setPixelColor(led_array[r][c], strip.Color(0, 0, 255, 0));
            break;
    }
}

//hideMove defintion
void led_hide_move(char x, char y) {
    int r = x - '0'; // convert ASCII
    int c = y - '0'; // convert ASCII

    strip.setPixelColor(led_array[r][c], strip.Color(0, 0, 0, 0)); // no color
} 

// update definition
void led_update() {
    strip.show(); // show strip
}

void led_clear() {
    for (int i = 0; i < 64; i++) {
		led_hide_move((i / 8) + '0', (i % 8) + '0');
	}

	led_update();
}