import serial
import matplotlib.pyplot as plt

ser = serial.Serial('COM3', 9600) # Cambia el nombre del puerto según corresponda

temperatura_valores = []
humedad_valores = []

plt.ion()
fig, ax = plt.subplots()

while True:
    try:
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        if line:
            valores = line.split()
            temperatura = float(valores[1][:-2])
            humedad = float(valores[3][:-1])
            
            temperatura_valores.append(temperatura)
            humedad_valores.append(humedad)
            
            ax.clear()
            ax.plot(temperatura_valores, label='Temperatura (C)')
            ax.plot(humedad_valores, label='Humedad (%)')
            ax.legend()
            plt.title("Temperatura y Humedad")
            plt.draw()
            plt.pause(0.1)
    except KeyboardInterrupt:
        break
        
ser.close()
