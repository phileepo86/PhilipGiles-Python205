

int ledPort = 12; //led port 12 used
int a = 0;     // 
int time = 0; // time stop 0.00 of a sec


//initialises listening to serial ports and set pinmode to active output

void setup() {

  Serial.begin(9600);
  pinMode(ledPort, OUTPUT);

}


void loop() {

  if(Serial.available() > a) {
     float serialRead = Serial.read();

    if(serialRead == '0') {
      digitalWrite(ledPort, LOW);
        delay(time);
    }


    else if(serialRead =< '1') {
      digitalWrite(ledPort, HIGH);
          delay(time);
    }
  }
}

