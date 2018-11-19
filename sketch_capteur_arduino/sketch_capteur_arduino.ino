const byte TRIGGER_PIN1 = 4;
const byte TRIGGER_PIN2 = 9;
const byte ECHO_PIN1    = 3;
const byte ECHO_PIN2    = 8;

const unsigned long MEASURE_TIMEOUT = 25000UL;

void setup() {
// put your setup code here, to run once:
Serial.begin(115200);

pinMode(TRIGGER_PIN1, OUTPUT);
pinMode(TRIGGER_PIN2, OUTPUT);
digitalWrite(TRIGGER_PIN1, LOW);
digitalWrite(TRIGGER_PIN2, LOW);
pinMode(ECHO_PIN1, INPUT);
pinMode(ECHO_PIN2, INPUT);
}

void loop() {

digitalWrite(TRIGGER_PIN1, HIGH);
delayMicroseconds(10);
digitalWrite(TRIGGER_PIN1, LOW);

long mesure1 = pulseIn(ECHO_PIN1, HIGH, MEASURE_TIMEOUT);
delayMicroseconds(5);

digitalWrite(TRIGGER_PIN2, HIGH);
delayMicroseconds(10);
digitalWrite(TRIGGER_PIN2, LOW);                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  

long mesure2 = pulseIn(ECHO_PIN2, HIGH, MEASURE_TIMEOUT);

float distance1 = mesure1 /58;
float distance2 = mesure2 /58;

String separ = ":";
String liste = distance1 + separ + distance2;

 Serial.println(liste);

 delay(50);
}

float moyenagedistance(float mesure, int iteration){
float result;
float dt = dt + mesure;
result = dt/iteration; 
return result;
}

