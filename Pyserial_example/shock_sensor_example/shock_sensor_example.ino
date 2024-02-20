// Define the shock sensor
int shock = 3
int val; // define a numeric variable val 

void setup () {
   // initialize serial communication:
  Serial.begin(9600);
  // input from KY-002 sensor
	pinMode (shock, INPUT); 
} 

void loop () {
	val = digitalRead (shock); // read the value from KY-002
  delay(500);
  Serial.print("State: ");
	if (val == HIGH ) {// when sensor detects shock, LED flashes  
    Serial.print("High");
	} else {
		Serial.print("Low");
	}
  Serial.print("\n");
  Serial.flush();
}

/* References: 
  1. https://arduinomodules.info/ky-002-vibration-switch-module/
  2. https://stackoverflow.com/questions/24074914/python-to-arduino-serial-read-write
 */