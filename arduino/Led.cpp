// This is the Led Hardware Library 
// for use with the ChessMate Project

// Source File

#include "Arduino.h"
#include "Led.h"

void Led::startStrip() {
    strip = Adafruit_NeoPixel(NUM_LEDS, PIN, NEO_GRBW + NEO_KHZ800);
    strip.begin();
    strip.show();
}

void Led::showMove(char x, char y) {
    int r = x - '0';
    int c = y - '0'; 
    strip.setPixelColor(led_array[r][c], 0, 0, 0, 50);
}

void Led::hideMove(char x, char y) {
    int r = x - '0';
    int c = y - '0'; 
    strip.setPixelColor(led_array[r][c], 0, 0, 0, 0);
} 

void Led::update() {
    strip.show();
}