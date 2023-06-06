import serial
ser = serial.Serial(port='/dev/cu.usbmodem101',baudrate=9600)

while True:
    data = str(ser.readline())
    dis = data.strip("b'\r\n")
    dis = float(dis[0:-4])
    print(dis)
    