import cv2
import pyautogui
import os
from datetime import datetime
import getpass

# Function to capture webcam photo
def capture_webcam_photo(output_dir):
    try:
        cam = cv2.VideoCapture(0)
        if not cam.isOpened():
            print("Error: Webcam not accessible.")
            return
        ret, frame = cam.read()
        if ret:
            filename = os.path.join(output_dir, f"webcam_{getpass.getuser()}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg")
            cv2.imwrite(filename, frame)
            print(f"Webcam photo saved: {filename}")
        else:
            print("Error: Unable to capture webcam image.")
        cam.release()
    except Exception as e:
        print(f"Webcam capture error: {e}")

# Function to capture screenshot
def capture_screenshot(output_dir):
    try:
        screenshot = pyautogui.screenshot()
        filename = os.path.join(output_dir, f"screenshot_{getpass.getuser()}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
        screenshot.save(filename)
        print(f"Screenshot saved: {filename}")
    except Exception as e:
        print(f"Screenshot capture error: {e}")

# Main script
def main():
    # Set custom directory for saving images
    output_dir = "D:\\CapturedImages"  # Change this path to your preferred location
    os.makedirs(output_dir, exist_ok=True)
    print(f"Saving images to: {output_dir}")

    capture_webcam_photo(output_dir)
    capture_screenshot(output_dir)

if __name__ == "__main__":
    main()
