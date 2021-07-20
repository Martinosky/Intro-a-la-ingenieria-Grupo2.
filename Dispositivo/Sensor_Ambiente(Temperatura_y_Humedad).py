import time
import board
import adafruit_dht
#Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D17)
while True:
    try:
         # Print the values to the serial port
         temperature_c = dhtDevice.temperature
         temperature_f = temperature_c * (9 / 5) + 32
         humidity = dhtDevice.humidity
         if humidity<50:
             print("Precaución: Falta Humedad en el ambiente") #Esto se hace manual
         elif humidity>70:
             print("Precaución: Exceso de humedad en el ambiente") #En este caso lo unico que hay que hacer es no regar
         if temperature_c<15:
             print("Precaución: Ausencia de Calor, pues se debe prender resistencia") #Aca se deberia prender automaticamente, pero por ahora es manual
         elif temperature_c>32:
             print("Precaución: Exceso de Calor, pues se debe apagar resistencia") 
         print("Temp: {:.1f} F / {:.1f} C    Humidity: {}% "
               .format(temperature_f, temperature_c, humidity))
    except RuntimeError as error:     # Errors happen fairly often, DHT's are hard to read, just keep going
         print(error.args[0])
    time.sleep(2.0)
