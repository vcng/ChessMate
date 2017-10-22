#include "protocol.h"
#include "integrate.h"
#include "led.h"

//Initialize Protocol
void protocol_init() {
    //Start serial port with our default baud rate
    Serial.begin(115200);  
    String input = "";
    
    //While loop to poll serial for start command to sync the devices
    while (true) {
        input = Serial.readString();
        input.trim();
        if (input == "start") {
            Serial.println("go");
            return;
        }
    }
}

//Toggle Command
void protocol_toggle(int r, int c) {
   //s is the output string, t is for toggle
   String s = "t";
   //concat the r (row) and c (column)
   s.concat(r);
   s.concat(c);
   Serial.println(s);
}

//Listen function
void protocol_listen() {
    //If there is something in the serial buffer
    if (Serial.available()) {
        //read the command section
        String cmd = Serial.readStringUntil(':');
        
        //count stores the count from serial command
        int count = 0;
        
        String out = "";

        //if led command
        if (cmd == "l") {
            //read led command
            cmd = Serial.readStringUntil(':');
            
            //if off command
            if (cmd == "0") {
                //get the count
                count = Serial.readStringUntil(':').toInt();
                cmd = Serial.readString();
                //for loop, runs count times and calls hide move on that coord
                for (int i = 0; i < count; i++) {
                    led_hide_move(cmd[i * 2 + 0], cmd[i * 2 + 1]);
                }
            }
            //if on command
            else if (cmd == "1") {
                //get the count
                count = Serial.readStringUntil(':').toInt();
                cmd = Serial.readString();
                //for loop, runs count times and calls the show move with the color and coord
                for (int i = 0; i < count; i++) {
                    led_show_move(cmd[i * 3 + 0], cmd[i * 3 + 1], cmd[i * 3 + 2]);
                }
            }
        //add else here for other commands when implemented
        }
        //light the leds
        led_update();
    }
}
