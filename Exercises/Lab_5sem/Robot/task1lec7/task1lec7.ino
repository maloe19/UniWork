int pin = A3;
int val = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  val = analogRead(pin);
  Serial.println(val);
  delay(2000);
}
