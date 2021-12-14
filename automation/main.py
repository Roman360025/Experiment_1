import serial

ser_sender = None
ser_receiver = None

while not ser_sender:
    try:
        ser_sender = serial.Serial(
            port='COM4',
            baudrate=115200,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=0)
    except:
        print('Unable to connect sender')

while not ser_receiver:
    try:
        ser_receiver = serial.Serial(
            port='COM6',
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

f = open('{}.txt'.format(sf), 'w')

while 1:
    ser_sender.write(b'%a\n\r' % power)
    ser_sender.write(b'%a\n\r' % sf)
    line_send = ser_sender.read(10000000000000000000000000000000000000)
    line_recv = ser_receiver.read(10000000000000000000000000000000000000)
    if line_recv != b'':
        f.write(line_recv.decode('utf-8'))
    if 'P' in line_send.decode('utf-8'):
        ser_sender.write(b'%a\n\r' % power)
        ser_sender.write(b'%a\n\r' % sf)
        ser_receiver.write(b'%a\n\r' % reset)
        power += 1

        if power == 14 and sf == 12:
            print('ALL')
            break
        elif power == 14:
            ser_receiver.write(b'%a\n\r' % sf)
            sf += 1
            power = -1
            f.close()
            f = open('{}.txt'.format(sf), 'w')


