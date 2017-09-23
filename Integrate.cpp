// This is the Integrated Hardware Library 
// for use with the ChessMate Project

// Source File

#include "Arduino.h"
#include "Integrate.h"

// Constructor definition
Integrate::Integrate()
{
  return;
}



// XOR definition
String Integrate::XOR(byte var1, byte var2)
{
  // var1 & var2 will be representing byte values
  // ex) (byte var1 = 23) => 00010111
  
  byte xor_total; // xor'd byte value of var1 ^ var2
  String final_byte; // final xor'd byte
  
  xor_total = var1 ^ var2; // XOR
  final_byte = String(xor_total);


  // OR //

  /*

  for(int i = 0; i <= 7; i++) {

    final_byte = final_byte + bitRead(total,i);
    // Read each bit of the byte based on position
    // & then append to a final string
  }

  */
  return final_byte;
}


// Coordinate definition
String Integrate::Coordinate()
{
  return;
}


