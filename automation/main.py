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
#
# while not ser_receiver:
#     try:
#         ser_sender = serial.Serial(
#             port='COM8',
#             baudrate=115200,
#             parity=serial.PARITY_NONE,
#             stopbits=serial.STOPBITS_ONE,
#             bytesize=serial.EIGHTBITS,
#             timeout=0)
#     except:
#         print('Unable to connect receiver')

print("connected to: " + ser_sender.portstr)

power = -1
sf = 7

while 1:
    line = ser_sender.read(10000000000000000000000000000000000000)
    if line != b'':
        print(line)
    if 'P' in line.decode('utf-8'):
        ser_sender.write(b'%a\n\r' % power)
        ser_sender.write(b'%a\n\r' % sf)
        power += 1
        if power == 14:
            sf += 1
            power = -1

        if power == 14 and sf == 12:
            print('ALL')
            break
