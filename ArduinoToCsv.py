import serial
import csv

# Set up the serial connection (adjust the port as needed)
ser = serial.Serial('COM4', 9600, timeout=1)  # Change 'COM3' to your Arduino's port
ser.flush()

# Output file
output_file = "sensor_data.csv"

with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    while True:
        try:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').strip()
                values = line.split(',')
                if len(values) == 6:  # Ensure correct number of values
                    writer.writerow(values)
                    print(values) 
        except KeyboardInterrupt:
            print("Data collection stopped.")
            break
        except Exception as e:
            print(f"Error: {e}")
            break
