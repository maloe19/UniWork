//int pin = A5;
//---

int pin1 = 2;
int pin2 = 4;
int pin3 = 5;
int comOutInPin = A5;



void setup() {
  //pinMode(pin, INPUT);
  //Serial.begin(9600);
  //---
  
  pinMode(pin1,OUTPUT);
  pinMode(pin2,OUTPUT);
  pinMode(pin3,OUTPUT);
  pinMode(comOutInPin,INPUT_PULLUP);
  Serial.begin(9600);
  
}

void loop() {
  //Serial.println(analogRead(pin));
  //delay(1000); 
  //---
  /*
  readComOutIn(0, LOW, LOW, LOW);
  readComOutIn(1, LOW, LOW, HIGH);
  readComOutIn(2, LOW, HIGH, LOW);
  readComOutIn(3, LOW, HIGH, HIGH);
  readComOutIn(4, HIGH, LOW, LOW);
  readComOutIn(5, HIGH, LOW, HIGH);
  readComOutIn(6, HIGH, HIGH, LOW);
  readComOutIn(7, HIGH, HIGH, HIGH);
  */
  readSwitch(0, LOW, LOW, LOW);
  readSwitch(1, LOW, LOW, HIGH);
  readSwitch(2, LOW, HIGH, LOW);
  readSwitch(3, LOW, HIGH, HIGH);
  readSwitch(4, HIGH, LOW, LOW);
  readSwitch(5, HIGH, LOW, HIGH);
  readSwitch(6, HIGH, HIGH, LOW);
  readSwitch(7, HIGH, HIGH, HIGH);
}


void readSwitch(int switchN, bool C, bool B, bool A) {
  digitalWrite(pin1, A);
  digitalWrite(pin2, B);
  digitalWrite(pin3, C);

  int channelValue = digitalRead(comOutInPin);

  if(channelValue == LOW){
    Serial.print(switchN);
    Serial.print(": ");
    Serial.println(digitalRead(comOutInPin));
    delay(1000);
  }
  
/*
  while (switchN == LOW){
    channelValue = digitalRead(comOutInPin);
  }
  */
}

/*
void readComOutIn(int channel, bool C, bool B, bool A){
  digitalWrite(pin1, A);
  digitalWrite(pin2, B);
  digitalWrite(pin3, C);
  
  boolean channelValue = digitalRead(comOutInPin);

  if(channel == LOW){
    Serial.println("Button ");
    Serial.println(channel);
    Serial.println(" was pushed!");
    delay(1000); 
  
  while(channel == LOW){
    channelValue = digitalRead(comOutInPin);
  }
}
*/
