#include "integrate.h"
#include "led.h"
#include "protocol.h"

void setup() {
  integrate_init();
  led_init();
  protocol_init();
}

void loop() {
  integrate_poll_hardware();
  protocol_listen();
}
