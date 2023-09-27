int led_pin1 =10;
int led_pin2 =2;
int blink_duration1 = 1000;
void setup() {


}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(led_pin1, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(blink_duration1);                      // wait for a second
  digitalWrite(led_pin1, LOW);   // turn the LED off by making the voltage LOW
  delay(blink_duration1);                   

    digitalWrite(led_pin2, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(blink_duration1);                      // wait for a second
  digitalWrite(led_pin2, LOW);   // turn the LED off by making the voltage LOW
  delay(blink_duration1);                        // wait for a second
}
