#include <Arduino.h>

#define BUTTON_PIN_16 16
#define BUTTON_PIN_17 17

void setup()
{
    Serial.begin(115200);
    pinMode(BUTTON_PIN_16, INPUT_PULLUP);
    pinMode(BUTTON_PIN_17, INPUT_PULLUP);
    Serial.println("ESP32 Ready");
}

void loop()
{
    if (digitalRead(BUTTON_PIN_16) == LOW)
    {
        Serial.println("CURSOR_UP");
        delay(200); // Debouncing delay
    }

    if (digitalRead(BUTTON_PIN_17) == LOW)
    {
        Serial.println("CURSOR_DOWN");
        delay(200); // Debouncing delay
    }

    delay(50); // Small delay for stability
}
