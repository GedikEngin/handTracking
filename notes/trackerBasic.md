#### 13/02/2024

installed libraries:

- #include <Mouse.h> (basic Arduino mouse library)
- #include <HID-Project.h> (for advanced mouse control, with potential keyboard usage)
- USBHost (as the HID (human interface device) library)

---

turns out esp32 devkit does not have usb hid system, need to use bluetooth to emulate it
looking at bluetooth setups to execute/try

BLEMouse by tvk stand alone doesnt work?
bringing in ble devices lib

- ESP32 BLE Arduino
- BLEMouse
- BLEKeyboard

keyboard doesnt work
trying different gpt and copilot prompts

still doesnt work. most likely due to HID

different approach being planned:

ESP32 is used to only send a trigger signal. the clicks and actions are executed from computer side.

---

use cpp script to send signals
use python script (using pyautogui) to execute linked commands to signal

working very well.
pygui responds fast to inputs by reading from serial port
esp32/cpp side can send correct signals consistently

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

pygui wiki
https://pyautogui.readthedocs.io/en/latest/
