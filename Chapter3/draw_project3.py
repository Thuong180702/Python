import serial
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ser = serial.Serial('COM3', 9600)
time.sleep(2)

temperature_data = []
humidity_data = []
timestamps = []

def read_sensor_data(framedata):
    data = ser.readline().decode().strip()
    print(data)

    if data:
        try:
            temperature, humidity = map(float, data.split(";"))
            temperature_data.append(temperature)
            humidity_data.append(humidity)
            timestamps.append(len(timestamps) + 1)
        except Exception as e:
            print("Error reading data from Arduino:", str(e))

    temperature_data_plot = temperature_data[-100:]
    humidity_data_plot = humidity_data[-100:]
    timestamps_plot = timestamps[-100:]

    ax.clear()
    ax.plot(timestamps_plot, temperature_data_plot, label='Temperature (°C)')
    ax.plot(timestamps_plot, humidity_data_plot, label='Humidity (%)')
    ax.set_xlim([max(0, len(timestamps_plot) - 50), len(timestamps_plot)])
    ax.set_ylim([0, 100])
    ax.set_title("DHT11 Readings")
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.legend()

fig = plt.figure()
ax = fig.add_subplot(111)
ani = animation.FuncAnimation(fig, read_sensor_data, interval=1000)

plt.show()
ser.close()
