#include <DHT.h>
#include <cvzone.h>

#define DHTPIN 12      // Pin connected to DHT11 data pin
#define DHTTYPE DHT11  // DHT11 sensor type

DHT dht(DHTPIN, DHTTYPE);

SerialData serialData;
int sendVals[2];

void setup() {
  Serial.begin(9600);
  Serial.println("DHT11 Sensor Test");
  dht.begin();
}

void loop() {
  delay(3000);  // Wait 2 seconds between readings\]

  float temperature = dht.readTemperature();  // Celsius
  float humidity = dht.readHumidity();

  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }
  sendVals[0] = int(temperature);
  sendVals[1] = int(humidity);
  serialData.Send(sendVals);

  // Serial.print("Humidity: ");
  // Serial.print(humidity);
  // Serial.print(" %\t");
  // Serial.print("Temperature: ");
  // Serial.print(temperature);
  // Serial.println(" °C");
}
