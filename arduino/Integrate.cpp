// This is the Integrated Hardware Library 
// for use with the ChessMate Project

// Source File

#include "Arduino.h"
#include "integrate.h"
#include "protocol.h"
#include "led.h"


//////////////////////////////////////////
//		  PRE-DEFINED VARIABLES			//
//////////////////////////////////////////

// Tells the D-flip flops chips to save state for reading
int newLatchPin[8] = {22, 23, 24, 25, 26, 27, 28, 29};

// These are the pins data is read from
int newDataPin[8] = {46, 47, 48, 49, 50, 51, 52, 53};

// This pin is used for iterating over data
int newClockPin = 32;			

// Holds the state of the board as bytes, 
// each bit is a col in a row
byte newBoard[64];

// Backup is same as newBoard, 
// used to compare to the state of newBoard
byte backup[64];

void integrate_wait_for_valid_start() {
	byte check_array[64] = {
		1,1,1,1,1,1,1,1,
		1,1,1,1,1,1,1,1,
		0,0,0,0,0,0,0,0,
		0,0,0,0,0,0,0,0,
		0,0,0,0,0,0,0,0,
		0,0,0,0,0,0,0,0,
		1,1,1,1,1,1,1,1,
		1,1,1,1,1,1,1,1
	};

	while (true) {
		integrate_poll_hardware();

		bool valid = true;
		for (int i = 0; i < 64; i++) {
			if (newBoard[i] != check_array[i]) {
				valid = false;
				led_show_move('r', (i / 8) + '0', (i % 8) + '0');
			} else {
				led_show_move('g', (i / 8) + '0', (i % 8) + '0');
			}
		}

		led_update();

		if (valid) {
			break;
		}
	}

	for (int i = 0; i < 64; i++) {
		led_show_move('b', (i / 8) + '0', (i % 8) + '0');
	}

	led_update();
}

//initialize definition
void integrate_init() 
{
	for (int i = 0; i < 8; i++) {
		pinMode(newLatchPin[i], OUTPUT);
		pinMode(newDataPin[i], INPUT);
	}

	pinMode(newClockPin, OUTPUT);

	integrate_wait_for_valid_start();
}

// pollHardware function definition
void integrate_poll_hardware() 
{
	for (int pin = 0; pin < 8; pin++) {
	  shiftRegisterIn(newLatchPin[pin], pin);
	}
}
  
// shiftRegisterIn function definition
void shiftRegisterIn(int oe, int row) //int oe, refers to the latch pin.
{ 
	digitalWrite(oe, 1);
	delayMicroseconds(20);
	digitalWrite(oe, 0);
  
	digitalWrite(newClockPin, 0);
	delayMicroseconds(20);
	
	// Read all 64 pins to see if they are true (1) or false (0), then set them
	for (int pin = 0; pin < 8; pin++) {
		if (digitalRead(newDataPin[pin])) {
			newBoard[row * 8 + pin] = 1;
		} else {
			newBoard[row * 8 + pin] = 0;
		}

		// Check for change
		if (newBoard[row * 8 + pin] != backup[row * 8 + pin]) {
			protocol_toggle((row * 8 + pin) / 8, (row * 8 + pin) % 8);
		}
  
		// Update the backup for future comparisons
		backup[row * 8 + pin] = newBoard[row * 8 + pin];
	}
	
	//Serial.print("\n");
	digitalWrite(newClockPin, 1);
	
	// Write the latch (oe pin)
	digitalWrite(oe, 1);
}