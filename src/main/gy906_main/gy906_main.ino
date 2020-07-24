/***************************************************
  This is a library example for the MLX90614 Temp Sensor

  Designed specifically to work with the MLX90614 sensors in the
  adafruit shop
  ----> https://www.adafruit.com/products/1747 3V version
  ----> https://www.adafruit.com/products/1748 5V version

  These sensors use I2C to communicate, 2 pins are required to
  interface
  Adafruit invests time and resources providing this open source code,
  please support Adafruit and open-source hardware by purchasing
  products from Adafruit!

  Written by Limor Fried/Ladyada for Adafruit Industries.
  BSD license, all text above must be included in any redistribution
 ****************************************************/

/*
   vin -> 3v
   gnd -> gnd
   scl -> A5
   sda -> A4
*/

#include <Wire.h>
#include <Adafruit_MLX90614.h>

Adafruit_MLX90614 mlx = Adafruit_MLX90614();

void setup() {
  Serial.begin(9600);


  mlx.begin();
}

void loop() {

  /*
    #######################################
    ## cating temp                       ##
    ## mlx.readObjectTempC() => the Temp ##
    #######################################
  */
  Serial.print(mlx.readAmbientTempC());
  Serial.print(" ");
  Serial.print(mlx.readObjectTempC());
  Serial.print("\n");


  /*
    ###########
    ## delay ##
    ###########
  */
  delay(500);
}
