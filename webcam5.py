import cv2
import mediapipe as mp
import serial
import time

# Initialize Serial Communication (Adjust "COM4" for your system)
arduino = serial.Serial("COM4", 9600, timeout=1)
time.sleep(2) 

# Initialize MediaPipe Hand Tracking
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Open webcam
cap = cv2.VideoCapture(0)

def fingers_extended(landmarks):
    """Determine which fingers are extended."""
    finger_states = [False] * 5  

    
    finger_states[0] = landmarks[4].x < landmarks[3].x  # Adjust for left/right hand

    # Other Fingers: Compare tip (8, 12, 16, 20) with PIP joint (6, 10, 14, 18)
    for i, tip, pip in [(1, 8, 6), (2, 12, 10), (3, 16, 14), (4, 20, 18)]:
        finger_states[i] = landmarks[tip].y < landmarks[pip].y  # Extended if above PIP joint

    return finger_states

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    command = None  # Initialize command

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Check which fingers are extended
            fingers = fingers_extended(hand_landmarks.landmark)
            thumb, index, middle, ring, pinky = fingers

            # Determine command based on hand state
            if all(fingers):  
                command = "O"  # Open gripper
            elif not any(fingers):  
                command = "C"  # Close gripper
            elif thumb and not index and not middle and not ring and not pinky:  
                command = "T"  # Thumb only (Servo 2 to 90°)
            elif thumb and index and not middle and not ring and not pinky:  
                command = "I"  # Thumb + Index (Servo 2 to 180°)

            # Send command to Arduino
            if command:
                arduino.write(command.encode())
                print(f"Sent: {command}")

    # Show the camera feed
    cv2.imshow("Hand Tracking", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
arduino.close()
