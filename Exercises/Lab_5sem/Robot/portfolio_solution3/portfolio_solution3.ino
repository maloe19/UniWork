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

//Motorshield pins:

  //Motor A (Left)
int motorLeftDirection = 12;   //DIR A
int motorLeftSpeed = 6;        //PWM A

  //Motor B (Right)
int motorRightDirection = 13;   //DIR B
int motorRightSpeed = 11;       //PWM B

//Booelans that determines whether the Robot is running or not.
boolean started = false;
boolean paused = false;


//Bytes that determine the State
byte startedState = B000;
byte pausedState = B001;
byte stoppedState = B010;
byte forwardState = B011;
byte leftState = B100;
byte rightState = B101;
byte backwardState = B110;

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

  //motorshield setup
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

  //"Clears" the EEPROM by setting all of the bytes in the EEPROM to 0.
  for (int i = 0 ; i < EEPROM.length() ; i++) {
    EEPROM.write(i, 0);
  }

  started = false;
  paused = false;
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

  int lengthOfList = addToEEPROM();

  if(started == true && paused == false){
    readList(lengthOfList);
    //while(true);
    //started = false;
  }
}


void writeShiftRegister(int output) {
  //Bring Latch Pin LOW - prepare to commit the register
  digitalWrite(latchPin, LOW);

  //Overwrites the entire register
  shiftOut(dataPin, clockPin, LSBFIRST, output);

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
      started = false;
      paused = false;
      //writeShiftRegister(stoppedState);
      for (int i = 0 ; i < EEPROM.length() ; i++) {
        EEPROM.write(i, 0);
        }
      drive(LOW, 0, LOW, 0, 0);
      Serial.print("Button ");
      Serial.print(channel);
      Serial.println(" was pushed!");
      Serial.println("Robot is turned off");
    }
    if (channel == 1){
      //set statePAUSED = TRUE
      paused = true;
      //writeShiftRegister(pausedState);
      Serial.print("Button ");
      Serial.print(channel);
      Serial.println(" was pushed!");
      //Serial.println("Robot is paused");
      while(paused == true){
        Serial.println("Robot is Paused! Press on Start to resume program!");
        delay(5000);
      }
      //delay(2000);
    }
    if ( channel == 2 ) {
      //set stateON = TRUE
      //writeShiftRegister(startedState);
      started = true;
      paused = false;
      Serial.print("Button ");
      Serial.print(channel);
      Serial.println(" was pushed!");
      Serial.println("Robot is started");
      delay(1000);
    }
    if ( channel == 3 ) {
      //set stateFORWARD = TRUE
      writeEEPROM(addToEEPROM(),forwardState);
      Serial.print("Button ");
      Serial.print(channel);
      Serial.println(" was pushed!");
      Serial.println(forwardState);
      delay(1000);
    }
    if ( channel == 4 ) {
      //set stateLEFT = TRUE
      writeEEPROM(addToEEPROM(),leftState);
      Serial.print("Button ");
      Serial.print(channel);
      Serial.println(" was pushed!");
      Serial.println(leftState);
      delay(1000);
    }
    if ( channel == 5 ) {
      //set stateRIGHT = TRUE
      writeEEPROM(addToEEPROM(),rightState);
      Serial.print("Button ");
      Serial.print(channel);
      Serial.println(" was pushed!");
      Serial.println(rightState);
      delay(1000);
    }
    if ( channel == 6 ) {
      //set stateBACKWARDS = TRUE
      writeEEPROM(addToEEPROM(),backwardState);
      Serial.print("Button ");
      Serial.print(channel);
      Serial.println(" was pushed!");
      Serial.println(backwardState);
      delay(1000);
  }
  /*
  //Loops until the button is not pressed anymore
  while(channelValue == LOW) {
    channelValue = digitalRead(comOutInPin);
  }
  */
  }
}

//Method for iterating and reading through the EEPROM
void readList(int length){
  for (int i = 0; i <= length; i++)
  {
    //delay(1000);
    byte data = EEPROM.read(i);
    if(data > 0){
      if(data == forwardState){
        //Go Forward
        writeShiftRegister(forwardState);
        Serial.print("Index ");
        Serial.print(i);
        Serial.println(" stores: ");
        readEEPROM(i);
        //Drive forward
        drive(HIGH, 100, HIGH, 100, 800);
        delay(1000);
      }
      if(data == leftState){
        //Turn Left (soft turn)
        writeShiftRegister(leftState);
        Serial.print("Index ");
        Serial.print(i);
        Serial.println(" stores: ");
        readEEPROM(i);
        //Turn left
        drive(HIGH, 0, HIGH, 100, 370);
        delay(1000);
      }
      if(data == rightState){
        //Turn Right (soft turn)
        writeShiftRegister(rightState);
        Serial.print("Index ");
        Serial.print(i);
        Serial.println(" stores: ");
        readEEPROM(i);
        //Turn right
        drive(HIGH, 100, HIGH, 0, 370);
        delay(1000);
      }
      if(data == backwardState){
        //Go Backwards
        writeShiftRegister(backwardState);
        Serial.print("Index ");
        Serial.print(i);
        Serial.println(" stores: ");
        readEEPROM(i);
        //Drive backwards
        drive(LOW, 70, LOW, 70, 800);
        delay(1000);
      }
    }
    else{
      started = false;
      drive(LOW, 0, LOW, 0, 0);
    }
  }
}

//Method that looks to see if started is true (if the start button has been pressed).
void isRunning(){
  if(started == true){
    readList(EEPROM.length());
  }
}

//Method that returns the index that is free, in order to insert something on that index.
int addToEEPROM(){
  for (int i = 0; i <= EEPROM.length(); i++){
    byte data = EEPROM.read(i);
    if(data == 0){
      return i;
    }
  }
}

//Method to clear the EEPROM.
void clearEEPROM(){
  //"Clears" the EEPROM by setting all of the bytes in the EEPROM to 0.
  for (int i = 0 ; i < EEPROM.length() ; i++) {
    EEPROM.write(i, 0);
  }
}
