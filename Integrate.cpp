// This is the Integrated Hardware Library 
// for use with the ChessMate Project

// Source File

#include "Arduino.h"
#include "Integrate.h"

//Constructor definition
Integrate::Integrate() {
	//define pin modes
	pinMode(this->latchPin, OUTPUT);	//shiftIn,Maw sets latchPin for OUTPUT, added this statement
   	pinMode(this->clockPin, OUTPUT);  	//shiftIn,Maw sets clockPin for OUTPUT, added this statement
	pinMode(this->dataPin, INPUT);	  	//shiftIn,Maw sets DataPin for INPUT,	added this statement
}

//readRows definition 
String Integrate::readRows() {
	String result = "";			//used for storing result of XOR
	
	for (int i = 0; i < 8; i++) {		//for each row in rows, XOR with sensor readings
		result = XOR(i);		//result = XOR(index of current row)
		return result;			//return result
	}
}

//XOR definition
String Integrate::XOR(int index) {
	
	byte temp = 0;
	byte result = 0;
	String coordinate = "";
	
	digitalWrite(this->latchPin,1);		//shiftIn,Maw tells the shift registers to save current states
	delay(20);				//shiftIn,Maw delay for the registers to save
	digitalWrite(this->latchPin,0);	  	//shiftIn,Maw tells the shift registers to hold data for reading

	temp = shiftIn(this->dataPin, this->clockPin);	//make temp hold current state on the row
	result = temp ^ rows[index];		//XOR current(temp) and the previous (rows[index])
	
	if (result == 0) {			//if the result is 0 then no change has been detected
		return "";			//return empty String
	} else {				//a change has been found
		rows[index] = temp;		//stores current(temp) in previously saved state (rows[index]) 

		int col = 7;			//start reading col at 7, because bytes are stored in reverse index vs an array

    		//for loop to find first (and only as of now) bit high and return the cord 
		for (int bit = 0; bit <= 7; bit++, col--) {	
      
      			//if the current bit is 1
			if (bitRead(result, bit) == 1) {			
				coordinate += index;	//append the index, row, to the coordinate String
				coordinate += " ";	//append a space
				coordinate += col;	//append col, or column, to the coordinate String
				
        		return coordinate;		//return coordinate
			}
		}
	}
}

//shiftIn,Maw this is the definition of the shiftIn function, only alterations are made for formatting.

////// ----------------------------------------shiftIn function
///// just needs the location of the data pin and the clock pin
///// it returns a byte with each bit in the byte corresponding
///// to a pin on the shift register. leftBit 7 = Pin 7 / Bit 0= Pin 0
byte Integrate::shiftIn(int myDataPin, int myClockPin) {
  int i;
  int temp = 0;
  int pinState;
  byte myDataIn = 0;

  pinMode(myClockPin, OUTPUT);
  pinMode(myDataPin, INPUT);

//we will be holding the clock pin high 8 times (0,..,7) at the
//end of each time through the for loop

//at the begining of each loop when we set the clock low, it will
//be doing the necessary low to high drop to cause the shift
//register's DataPin to change state based on the value
//of the next bit in its serial information flow.
//The register transmits the information about the pins from pin 7 to pin 0
//so that is why our function counts down
  for (i=7; i>=0; i--) {
    digitalWrite(myClockPin, 0);
    delayMicroseconds(0.2);
    temp = digitalRead(myDataPin);
    if (temp) {
      pinState = 1;
      //set the bit to 0 no matter what
      myDataIn = myDataIn | (1 << i);
    } else {
      //turn it off -- only necessary for debuging
     //print statement since myDataIn starts as 0
      pinState = 0;
    }

    //Debuging print statements
    //Serial.print(pinState);
    //Serial.print("     ");
    //Serial.println (dataIn, BIN);

    digitalWrite(myClockPin, 1);

  }
  //debuging print statements whitespace
  //Serial.println();
  //Serial.println(myDataIn, BIN);
  return myDataIn;
}
