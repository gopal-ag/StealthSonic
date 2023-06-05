
const int TRIG_PIN   = 6; 
const int ECHO_PIN   = 7; 
const int BUZZER_PIN = 3;
const int LED_PIN = 5; 
const int DISTANCE_THRESHOLD = 50; 


float duration_us, distance_cm;

void setup() {
  Serial.begin (9600);         
  pinMode(TRIG_PIN, OUTPUT);   
  pinMode(ECHO_PIN, INPUT);    
  pinMode(BUZZER_PIN, OUTPUT); 
}

void loop() {

  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(20);
  digitalWrite(TRIG_PIN, LOW);


  duration_us = pulseIn(ECHO_PIN, HIGH);

  distance_cm = 0.017 * duration_us;

  if(distance_cm < DISTANCE_THRESHOLD){
    digitalWrite(BUZZER_PIN, HIGH);
    digitalWrite(LED_PIN, HIGH); 
  }
    
  else
  {
    digitalWrite(BUZZER_PIN, LOW);
    digitalWrite(LED_PIN, LOW); 
  }
  
  Serial.print("distance: ");
  Serial.print(distance_cm);
  Serial.println(" cm");

  delay(500);
}

