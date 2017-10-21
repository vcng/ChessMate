// This is the Integrated Hardware Library 
// for use with the ChessMate Project

// Header File
#ifndef INTEGRATE_H
#define INTEGRATE_H

#include "Arduino.h"
#include "protocol.h"

/*
This function is used to setup the board to make sure that all the chess pieces are in the correct place.
Rows 0,1 and 6,7 are going to be a byte long each with 8 bits all equal to 1 and
Rows 2,3,4,5 are going to be a byte long each with 8 bits all equal to 0.
Once this sequence of bytes is correctly set up, 
this functon will return back to the protocol to allow the start of the game.
*/
void integrate_init();

// This is function keeps signaling the hardware to see if the there are any updates coming from the board,
// if so we can determine the changed bits form the 64 (8 * 8bytes) possible.
void integrate_poll_hardware();

// This function actually updates the bits given a certain row and the corresponding latch pin.
void shiftRegisterIn(int oe, int row);

#endif
