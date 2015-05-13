#include <DHT.h>
#include <Process.h>

//pins
int LDR_PIN = A5;
int MOI_PIN = A2;
int DHT_PIN = A0; //Pino DATA do Sensor ligado na porta Analogica A1


DHT dht(DHT_PIN, DHT11);

//storage vals
int ldr = 0;
int moi = 0;
float temp = 0;
float humd = 0;


void setup() {
  // Initialize Bridge
  Bridge.begin();

  // Initialize Serial
  Serial.begin(9600);

  // Wait until a Serial Monitor is connected.
  while (!Serial);
  dht.begin();
  
}

void loop() {
  ldr = analogRead(LDR_PIN);
  moi = analogRead(MOI_PIN);
  Serial.print("Light = ");
  Serial.println(ldr);
  Serial.print("Moisture = ");
  Serial.println(moi);
  Serial.print("Temperature: "); 
  temp = dht.readTemperature();
  Serial.println(temp);
  Serial.print("Humidity: ");  
  humd = dht.readHumidity();
  Serial.println(humd);
  Serial.println();
  
  runSender("LIGHT", String(ldr));
  delay(150);
  
  runSender("MOIST", String(moi));
  delay(150);

  runSender("TEMP", String(temp));
  delay(150);

  runSender("HUM", String(humd));
  delay(150);


  delay(1000);
}

void runSender(String type, String val) {
  Process p;		// Create a process and call it "p"
  p.begin("/root/yun_sender.py");	// Process that launch the "curl" command
  p.addParameter(type); // Add the URL parameter to "curl"
  p.addParameter(val); // Add the URL parameter to "curl"
  p.run();		// Run the process and wait for its termination

  // Print arduino logo over the Serial
  // A process output can be read with the stream methods
  while (p.available() > 0) {
    char c = p.read();
    Serial.print(c);
  }
  // Ensure the last bit of data is sent.
  Serial.flush();
}
