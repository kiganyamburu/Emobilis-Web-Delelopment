import cv2
import sys


def open_webcam():
    # Initialize video capture from default webcam (usually 0)
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened successfully
    if not cap.isOpened():
        print("Error: Could not open webcam")
        sys.exit()

    print("Webcam opened successfully")
    print("Press 'ESC' to quit")

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Check if frame is read correctly
        if not ret:
            print("Error: Can't receive frame")
            break

        # Display the frame
        cv2.imshow('Webcam Feed', frame)

        # Break the loop when ESC is pressed (key code 27)
        key = cv2.waitKey(1)
        if key == 27:  # ESC key
            break

    # Release the capture and destroy windows
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    open_webcam()