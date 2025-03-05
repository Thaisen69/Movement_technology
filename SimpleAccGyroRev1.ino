/*
  Arduino LSM9DS1 - Simple Accelerometer

  This example reads the acceleration values from the LSM9DS1
  sensor and continuously prints them to the Serial Monitor
  or Serial Plotter.

  The circuit:
  - Arduino Nano 33 BLE Sense

  created 10 Jul 2019
  by Riccardo Rizzo

  This example code is in the public domain.
*/

#include <Arduino_LSM9DS1.h>

void setup() {
  Serial.begin(9600);
  while (!Serial);
  Serial.println("Started");

  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }

  Serial.print("Accelerometer sample rate = ");
  Serial.print(IMU.accelerationSampleRate());
  Serial.println(" Hz");
  Serial.print("Gyroscope sample rate = ");
  Serial.print(IMU.gyroscopeSampleRate());
  Serial.println(" Hz");
  Serial.println();
  Serial.println("Acceleration in g's and Gyroscope in degrees/second");
  Serial.println("xA,yA,zA,xG,yG,zG");
}

void loop() {
  float xA, yA, zA, xG, yG, zG;

  if (IMU.accelerationAvailable()) {
    IMU.readAcceleration(xA, yA, zA);
    IMU.readGyroscope(xG, yG, zG);

    Serial.print(xA);
    Serial.print(',');
    Serial.print(yA);
    Serial.print(',');
    Serial.print(zA);
    Serial.print(',');
    Serial.print(xG);
    Serial.print(',');
    Serial.print(yG);
    Serial.print(',');
    Serial.println(zG);
  }
}
