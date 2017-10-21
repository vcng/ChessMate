#ifndef __SERIALTEST_H
#define __SERIALTEST_H

#include <Arduino.h>
#include <string.h>

void protocol_init();
void protocol_toggle(int x, int y);
void protocol_listen();

#endif