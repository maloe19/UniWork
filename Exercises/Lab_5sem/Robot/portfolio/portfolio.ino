//Includes the EEPROM library
#include <EEPROM.h>

//Multiplexer Pins
int pinA = 3; //Blue
int pinB = 4; //Green
int pinC = 5; //Yellow
int comOutInPin = A5; //White

//ShiftRegister Pins
int latchPin = 7; //ST_CP or RCLK
int clockPin = 8; //SH_CP or SRCLK
int dataPin = 9; //DS or SER

//motorshield 40x40 pins
 //Motor A (Left)
int motorLeftDirection = 12;   //DIR A
int motorLeftSpeed = 6;        //PWM A

//Motor B (Right)
int motorRightDirection = 13;   //DIR B
int motorRightSpeed = 11;       //PWM B


/*
12,9,13 og 8 til motor
2 og 6(den nye 3) til tako
0 og 1 skal ikke bruge (bruges til serial)
8 og 9 kan bruges til andet - breakfunktion

Liste(6): 3, 4, 5, 7, 10,11
*/

void setup() {
  pinMode(pinA, OUTPUT);
  pinMode(pinB, OUTPUT);
  pinMode(pinC, OUTPUT);
  pinMode(comOutInPin, INPUT_PULLUP);

  Serial.begin(9600);

  //motorshield 40x40 setup
    //Motor A (Left)
  pinMode(motorLeftDirection, OUTPUT);
  pinMode(motorLeftSpeed, OUTPUT);
  
  //Motor B (Right)
  pinMode(motorRightDirection, OUTPUT);
  pinMode(motorRightSpeed, OUTPUT);

  //shiftregister setup
    //Set pins to output so you can control the shift register
  pinMode(latchPin, OUTPUT);
  pinMode(clockPin, OUTPUT);
  pinMode(dataPin, OUTPUT);

  digitalWrite(latchPin, LOW);
  digitalWrite(clockPin, LOW);
  digitalWrite(dataPin, LOW);
}

void loop() {
  readComOutIn(0, LOW, LOW, LOW);
  readComOutIn(1, LOW, LOW, HIGH);
  readComOutIn(2, LOW, HIGH, LOW);
  readComOutIn(3, LOW, HIGH, HIGH);
  readComOutIn(4, HIGH, LOW, LOW);
  readComOutIn(5, HIGH, LOW, HIGH);
  readComOutIn(6, HIGH, HIGH, LOW);
  readComOutIn(7, HIGH, HIGH, HIGH);
}


void writeShiftRegister(int output) {
  //Bring Latch Pin LOW - prepare to commit the register
  digitalWrite(latchPin, LOW);

  //Overwrites the entire register
  shiftOut(dataPin, clockPin, MSBFIRST, output);

  //Bring Latch Pin HIGH - commits the register
  digitalWrite(latchPin, HIGH);
}

//Drives the robot
void drive(boolean leftDirection, int leftSpeed, boolean rightDirection, int rightSpeed, int distance) {
  //Motor A (Left)
  digitalWrite(motorLeftDirection, leftDirection);
  digitalWrite(motorLeftSpeed, leftSpeed);
  
  //Motor B (Right)
  digitalWrite(motorRightDirection, rightDirection);
  digitalWrite(motorRightSpeed, rightSpeed);

  //Driving distance/time
  delay(distance);
}

//Stores a char in EEPROM
void writeEEPROM(int address, byte data) {
  EEPROM.write(address, data);
}

//Read a char from EEPROM
void readEEPROM(int address) {
  byte data = EEPROM.read(address);
  Serial.println(data);
}

//Detects button input
void readComOutIn(int channel, bool C, bool B, bool A) {
  //Defines which channel the comOutIn port is connected to
  digitalWrite(pinA, A);
  digitalWrite(pinB, B);
  digitalWrite(pinC, C);

  //Reads the channel
  boolean channelValue = digitalRead(comOutInPin);

  //If the connected button is pushed
  if(channelValue == LOW) {
    if ( channel == 0 ) {
      //set stateOFF = TRUE
      //writeShiftRegister(B00000000);
      writeEEPROM(0,000);
          Serial.print("Button ");
    Serial.print(channel);
    Serial.println(" was pushed!");
       delay(2000);
       readEEPROM(0);
       while(true);
    }
      if ( channel == 2 ) {
      //set stateON = TRUE
      //writeShiftRegister(B00000010);
      writeEEPROM(2,010);
          Serial.print("Button ");
    Serial.print(channel);
    Serial.println(" was pushed!");
       delay(2000);
      readEEPROM(2);
      while(true);
  }
      if ( channel == 3 ) {
      //set stateFORWARD = TRUE
      //writeShiftRegister(B00000011);
      writeEEPROM(3,011);
          Serial.print("Button ");
    Serial.print(channel);
    Serial.println(" was pushed!");
       delay(2000);
       readEEPROM(3);
       while(true);
       //Go Forward
       drive(HIGH, 100, HIGH, 100, 800);

  }
      if ( channel == 4 ) {
      //set stateLEFT = TRUE
      //writeShiftRegister(B00000100);
      writeEEPROM(4,100);
          Serial.print("Button ");
    Serial.print(channel);
    Serial.println(" was pushed!");
       delay(2000);
       readEEPROM(4);
       while(true);
       //Turn Left (soft turn)
       drive(HIGH, 0, HIGH, 100, 370);
  }
      if ( channel == 5 ) {
      //set stateRIGHT = TRUE
      //writeShiftRegister(B00000101);
      writeEEPROM(5,101);
          Serial.print("Button ");
    Serial.print(channel);
    Serial.println(" was pushed!");
       delay(2000);
       readEEPROM(5);
       while(true);
       //Turn Right (soft turn)
       drive(HIGH, 100, HIGH, 0, 370);

  }
      if ( channel == 6 ) {
      //set stateBACKWARDS = TRUE
      //writeShiftRegister(B00000110);
      writeEEPROM(6,110);
          Serial.print("Button ");
    Serial.print(channel);
    Serial.println(" was pushed!");
       delay(2000);
       readEEPROM(6);
       while(true);
       //Go Backwards
       drive(LOW, 70, LOW, 70, 800);
  }
      else {
      //set statePAUSED = TRUE
      //writeShiftRegister(B00000001);
       delay(2000);
  }
  

    
    Serial.print("Button ");
    Serial.print(channel);
    Serial.println(" was pushed!");
    delay(100);
  
  

  //Loops until the button is not pressed anymore
  while(channelValue == LOW) {
    channelValue = digitalRead(comOutInPin);
  }
}
}
