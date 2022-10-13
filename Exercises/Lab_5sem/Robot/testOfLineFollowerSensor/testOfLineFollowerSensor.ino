int analogPin = A5; 
int val = 0;
int leftsensor = 0;
int rightsensor = 0;
int middlesensor = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(analogPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  val = analogRead(analogPin);
  Serial.println(val);
  delay(1000);
}
/*
void difference(){ 
  if(leftsensor>=700 && rightsensor<700){
    RIGHT();
  } 
  if(rightsensor>=700 && leftsensor<700){
    LEFT();
  } 
  if(middlesensor>=700 && rightsensor<700 && leftsensor<700){
    FORWARD();
  }
  if(middlesensor<700 && rightsensor<700 && leftsensor<700){
    UTURN();
  }
}
*/
