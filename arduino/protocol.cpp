#include "protocol.h"
#include "integrate.h"
#include "led.h"

void protocol_init() {
    Serial.begin(115200);  
    String input = "";

    while (true) {
        input = Serial.readString();
        input.trim();
        if (input == "start") {
            Serial.println("go");
            return;
        }
    }
}

void protocol_toggle(int x, int y) {
   String s = "t";
   s.concat(x);
   s.concat(y);
   Serial.println(s);
}

void protocol_listen() {
    if (Serial.available()) {
        String cmd = Serial.readStringUntil(':');
        int count = 0;
        String out = "";

        //if led command
        if (cmd == "l") {
            cmd = Serial.readStringUntil(':');
            if (cmd == "0"){
                count = Serial.readStringUntil(':').toInt();
                cmd = Serial.readString();
                for (int i = 0; i < count; i++) {
                    led_hide_move(cmd[i * 2 + 0], cmd[i * 2 + 1]);
                }
            }
            //if on command
            else if (cmd == "1") {
                count = Serial.readStringUntil(':').toInt();
                cmd = Serial.readString();
                for (int i = 0; i < count; i++) {
                    led_show_move(cmd[i * 3 + 0], cmd[i * 3 + 1], cmd[i * 3 + 2]);
                }
            }
        //add else here for other commands when implemented
        }

        led_update();
    }
}