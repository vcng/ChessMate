// This is the Integrated Hardware Library 
// for use with the ChessMate Project

// Header File
#ifndef INTEGRATE_H
#define INTEGRATE_H


#include "Arduino.h"

class Integrate {
	private:
		int latchPin = 8;					//shiftin,Maw tells the shift registers to save state for reading
		
		int dataPin = 9; 					//shiftin,Maw this is the pin data is read from
		
		int clockPin = 7;					//shiftin,Maw this pin is used for iterating over data
		
		byte rows[8] = {B0, B0, B0, B0, B0, B0, B0, B0};	//holds the state of the board as bytes, each bit is a col in a row
		
	public:
		/*
		Default constructor for Integrate
		Sets up the pins for shiftin
		*/
		Integrate();
		
		/*
		XOR takes in the index of the row to be read, gets the current state of the row from the sensors,
		then does an XOR operation on the two bytes, the result is any changes that have occured. Using this
		we determine which column changed and return the row, col as a string in the form "r c" for output to the pi.
		*/
		String XOR(int index);
		/*
		readRows iterates over the rows of the board, currently stops when a change is found.
		*/
		String readRows();
		
		// 	This function is from a tutorial from Arduino, any code we use from this tutorial is not our own, nor do we claim so.
		//	To better document where sources came from we will add shiftIn,Maw as a tag, which refers to the link and relevant 
		//	info below as the original creator.
		// 	https://www.arduino.cc/en/Tutorial/ShftIn21?action=sourceblock&num=1
		//**************************************************************//
		//  Name    : shiftIn Example 2.1                               //
		//  Author  : Carlyn Maw                                        //
		//  Date    : 25 Jan, 2007                                      //
		//  Version : 1.0                                               //
		//  Notes   : Code for using a CD4021B Shift Register    		//
		//          :                                                   //
		//****************************************************************
		byte shiftIn(int myDataPin, int myClockPin);
};

#endif
