// Define the photoresistor 
int photo = 3;
int val; // define a numeric variable val 

void setup () {
   // initialize serial communication:
  Serial.begin(9600);
  // input from KY-photoresistor
	pinMode (photo, INPUT); 
} 

void loop () {
	val = analogRead(photo); // read the value from KY-002
  Serial.print("Value: ");
  Serial.println(val, DEC);
  Serial.flush();
  delay(50);
}

/* References: 
  1. https://arduinomodules.info/ky-002-vibration-switch-module/
  2. https://stackoverflow.com/questions/24074914/python-to-arduino-serial-read-write
 */