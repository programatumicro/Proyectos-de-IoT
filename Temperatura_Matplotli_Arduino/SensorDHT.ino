#include <DHT.h>
#define DHTPIN 2
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  float temperatura = dht.readTemperature();
  float humedad = dht.readHumidity();
  
  Serial.print("Temperatura: ");
  Serial.print(temperatura);
  Serial.print("°C");

  Serial.print(" Humedad: ");
  Serial.print(humedad);
  Serial.println("%");

  delay(5000);
}
