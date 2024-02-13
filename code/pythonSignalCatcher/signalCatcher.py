import serial # pip install pyserial
import pyautogui

# Update COM_PORT to the correct port for your ESP32
COM_PORT = 'COM5'  # Example: 'COM3' on Windows or '/dev/ttyUSB0' on Linux
BAUD_RATE = 115200

def main():
    with serial.Serial(COM_PORT, BAUD_RATE, timeout=1) as ser:
        print("Listening for button presses...")
        while True:
            line = ser.readline().decode('utf-8').strip()

            # mouse clicks
            if line == "LEFT_CLICK":
                pyautogui.click(button='left')
                print("Left click triggered")

            elif line == "RIGHT_CLICK":
                pyautogui.click(button='right')
                print("Right click triggered")

            # mouse movement
            elif line == "CURSOR_UP":
                pyautogui.move(0, -50)
                print("Cursor up triggered")

            elif line == "CURSOR_DOWN":
                pyautogui.move(0, 50)
                print("Cursor down triggered")

            elif line == "CURSOR_LEFT":
                pyautogui.move(-50, 0)
                print("Cursor left triggered")

            elif line == "CURSOR_RIGHT":
                pyautogui.move(50, 0)
                print("Cursor right triggered")

            # scrolling

            elif line == "SCROLL_UP":
                pyautogui.scroll(10)
                print("Scroll up triggered")

            elif line == "SCROLL_DOWN":
                pyautogui.scroll(-10)
                print("Scroll down triggered")

        

if __name__ == "__main__":
    main()
