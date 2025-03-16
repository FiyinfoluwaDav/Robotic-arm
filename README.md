Two-Servo Robotic Arm

1 Overview 
This project is a simple robotic arm controlled by two servo motors:  
- One servo controls the gripping mechanism (opening and closing).  
- The other servo controls the rotation of the arm.  

The project is designed for basic object manipulation and can be expanded for automation and AI-based control.  

## Hardware Requirements 
- Microcontroller: Arduino Uno/Nano  
- Servos: SG90 / MG995 (or any compatible servo motors)  
- Power Supply: 5V battery pack or external adapter  
- Frame: 3D-printed/plastic/wood  
- Jumper Wires  

## Software Requirements  
- Arduino IDE (for programming the microcontroller)  
- Servo Library (included in Arduino by default)
- Python Mediapipe library
- OpenCV

## Installation & Setup  
 
2. Connect the servo motors:  
   - Rotation Servo → Pin 9  
   - Gripper Servo → Pin 10  
   - Power the servos from the 5V and GND of the Arduino  

3. Upload the code:  
   - Open `Gripper_4.ino` in Arduino IDE  
   - Select the correct Board** and Port  
   - Click Upload
   - Run the webcam5.py code (Ensure you check which port your microcontroller is connected to and edit it in the webcam5.py code)

## Usage 
- The arm rotates when given a command.  
- The gripper opens/closes to pick up objects.  
- Modify the code to add button control, joystick control, or serial commands for interaction.  



## Contributing 
Feel free to fork this project, submit pull requests, or report issues.  
