//int analogPin = A5;
//int val = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(3,INPUT);
  //Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(3, HIGH);
  delay(5000);            
  digitalWrite(3, LOW);  
   delay(1000);  

  //val = analogRead(analogPin); 
  //analogWrite(3, val / 4);
  //Serial.println(val);
}

//5*1000/1000+1000
