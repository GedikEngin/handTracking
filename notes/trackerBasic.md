#### 13/02/2024

installed libraries:

- #include <Mouse.h> (basic Arduino mouse library)
- #include <HID-Project.h> (for advanced mouse control, with potential keyboard usage)
- USBHost (as the HID (human interface device) library)

---

turns out esp32 devkit does not have usb hid system, need to use bluetooth to emulate it
looking at bluetooth setups to execute/try

## important resources:

arduino's standard mouse libs
https://www.arduino.cc/reference/en/language/functions/usb/mouse/
https://www.arduino.cc/reference/tr/language/functions/usb/mouse/mouseclick/
https://www.arduino.cc/reference/tr/language/functions/usb/mouse/mouseend/
https://www.arduino.cc/reference/tr/language/functions/usb/mouse/mousemove/
https://github.com/arduino-libraries/Mouse/blob/master/src/Mouse.cpp

advanced io control lib
https://github.com/NicoHood/HID?utm_source=platformio&utm_medium=piohome

esp32 info/spec sheet
https://docs.espressif.com/projects/esp-idf/en/latest/esp32/hw-reference/esp32/get-started-devkitc.html

#include <HID.h>
#include <Arduino.h>
#include <Mouse.h>
#include <HID-Project.h>

const int leftButtonPin = 16;
const int rightButtonPin = 17;

void setup()
{
pinMode(leftButtonPin, INPUT_PULLDOWN);
pinMode(rightButtonPin, INPUT_PULLDOWN);
Mouse.begin();
}

void loop()
{
// clicks MOUSE_LEFT if it receives signal from leftButtonPin
if (digitalRead(leftButtonPin) == HIGH)
{
Mouse.click(MOUSE_LEFT);
}

// clicks MOUSE_RIGHT if it receives signal from rightButtonPin
if (digitalRead(rightButtonPin) == HIGH)
{
Mouse.click(MOUSE_RIGHT);
}

Mouse.end();
}

// srcs notes:
// button: which mouse button to press (MOUSE_LEFT, MOUSE_RIGHT, MOUSE_MIDDLE, default = MOUSE_LEFT)
