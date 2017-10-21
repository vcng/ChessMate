#include "integrate.h"
#include "led.h"
#include "protocol.h"

void setup() {
  led_init();
  integrate_init();
  protocol_init();
  led_clear();
}

void loop() {
  integrate_poll_hardware();
  protocol_listen();
}
