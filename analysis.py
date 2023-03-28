import serial

ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with the port your Arduino is connected to

while True:
    data = ser.readline().decode('utf-8').rstrip()  # Read data from Arduino
    if data:
        print(data)  # Print the data to the console
        # Process the data however you like here
