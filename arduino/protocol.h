#ifndef __SERIALTEST_H
#define __SERIALTEST_H

#include <Arduino.h>
#include <string.h>

//Initialize function for protocol
void protocol_init();

//Toggle command
void protocol_toggle(int x, int y);

//Listener for recieving input from serial
void protocol_listen();

#endif
