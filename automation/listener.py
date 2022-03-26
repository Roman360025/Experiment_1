import serial
import datetime

ser_receiver = None

while not ser_receiver:
    try:
        ser_receiver = serial.Serial(
            port='COM13',
            baudrate=115200,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=0)
    except:
        print('Unable to connect receiver')

print("connected to: " + ser_receiver.portstr)

power = -1
sf = 7
reset = 0

line = ''

filename = 'Experiment_data/Experiment_10_packets'

now = datetime.datetime.now().strftime('%Y-%m-%d')

with open(f'{filename}_{now}.txt', 'a') as f:
    while 1:
        try:
            line_recv = ser_receiver.read(10000000000000000000000000000000000000)
            if line_recv != b'':
                received_line = line_recv.decode('utf-8')
                line = line + received_line
                f.write(received_line)
            if '\n' in line:
                print(line)
                line = ''
        except:
            break



