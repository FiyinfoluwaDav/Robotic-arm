#include <Servo.h>

Servo servo1;  // Gripper
Servo servo2;  // Rotation

void setup() {
    Serial.begin(9600);
    servo1.attach(9);  // Pin for Gripper Servo
    servo2.attach(10); // Pin for Rotation Servo
}

void loop() {
    if (Serial.available() > 0) {
        char command = Serial.read();  // Read the command

        if (command == 'O') {
            servo1.write(0);  // Open Gripper
            Serial.println("Gripper Opened");
        }
        else if (command == 'C') {
            servo1.write(180);  // Close Gripper
            Serial.println("Gripper Closed");
        }
        else if (command == 'T') {
            servo2.write(0);  // Rotate to 90°
            Serial.println("Servo 2 at 90°");
        }
        else if (command == 'I') {
            servo2.write(180);  // Rotate to 180°
            Serial.println("Servo 2 at 180°");
        }
    }
}
