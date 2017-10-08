#define SIZE 64
#define LED_COUNT 64
#define LED_PIN 52

#include <Adafruit_NeoPixel.h>

// Board pin mapping
static const byte BOARD_PINS[] = {
  43, 43, 43, 43, 43, 43, 43, 43,
  43, 43, 43, 43, 43, 43, 43, 43,
  43, 43, 25, 43, 43, 43, 43, 43,
  43, 43, 24, 43, 43, 43, 43, 43,
  43, 43, 23, 43, 43, 43, 43, 43,
  43, 43, 22, 43, 43, 43, 43, 43,
  43, 43, 43, 43, 43, 43, 43, 43,
  43, 43, 43, 43, 43, 43, 43, 43
};

byte board[SIZE];
byte backup[SIZE];

Adafruit_NeoPixel strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, NEO_GRBW + NEO_KHZ800);

void setup() {
  // Begin serial communication
  Serial.begin(9600);

  // Set all pins to input
  for (int pin = 0; pin < SIZE; pin++) {
    pinMode(BOARD_PINS[pin], INPUT);
  }

  // Initialize board data
  for (int i = 0; i < SIZE; i++) {
    board[i] = 0;
    backup[i] = 0;
  }

  board[18] = 1;
  backup[18] = 1;
  

  // Initialize LED strip
  strip.begin();
  strip.show();
}

// Convert a row, col to an LED strip index
// in the following (reduced) pattern:
// 0 1 2
// 5 4 3
// 6 7 8
int coordToIndex(int row, int col) {
  if (row % 2 == 0) {
    return row * 8 + col;
  } else {
    return (row + 1) * 8 - col - 1;
  }
}

void loop() {
  //strip.setPixelColor(14, strip.Color(255, 0, 0, 0));
  //strip.show();
  pollHardware();
  pollController();
  
  delay(100);
}

void pollHardware() {
  // For each pin being polled
  for (int pin = 0; pin < SIZE; pin++) {
    // Read the pin
    board[pin] = digitalRead(BOARD_PINS[pin]);

    // If the pin value changed since last poll
    if (board[pin] != backup[pin]) {
      // Send an update to the pi
      Serial.print("t ");
      Serial.print(pin / 8);
      Serial.print(" ");
      Serial.print(pin % 8);
      Serial.print("\n");

      // Record the value for future comparison
      backup[pin] = board[pin];
    }
  }
}

void pollController() {
  // If there is any serial communication available
  while (Serial.available() > 0) {
    // Read the command string
    String cmd = Serial.readStringUntil(':');

    // If the command is an on/off command
    if (cmd == "on" || cmd == "off") {

      // Get the affected coordinate count
      int count = Serial.readStringUntil(':').toInt();

      // Read each affected coordinate
      for (int i = 0; i < count; i++) {
        int row = Serial.readStringUntil(':').toInt();
        int col = Serial.readStringUntil(':').toInt();

        // For debugging, echo the command to the pi for now
        Serial.print("debug: ");
        Serial.print(cmd);
        Serial.print(" ");
        Serial.print(row);
        Serial.print(" ");
        Serial.print(col);
        Serial.print("\n");

        // Execute the command on the LED strip
        if (cmd == "on") {
          strip.setPixelColor(coordToIndex(row, col), strip.Color(255, 0, 0, 0));
        } else if (cmd == "off") {
          strip.setPixelColor(coordToIndex(row, col), strip.Color(0, 0, 0, 0));
        }

        
      }

      // Show the update
      strip.show();
    }
  }
}

