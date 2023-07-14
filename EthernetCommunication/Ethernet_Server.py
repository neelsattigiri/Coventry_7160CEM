import socket
import pickle
import Test

test = Test.confdata

vehicleSpd = test.vehicleSpd
vehicleAng = test.vehicleAng
vehicleType = test.vehicleType

AccelPedlPos = test.AccelPedlPos
Transmission = test.Transmission
PowerControlStatus = test.PowerControlStatus
IsFailure = test.IsFailure
IsSafetyOn = test.IsSafetyOn

# take the server name and port name
host = 'local host'
port = 5000
# create a socket for server
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

# bind socket to server
s.bind(('', port))

# allow  1 connection
s.listen(1)

# wait till a client accepts

c, addr = s.accept()

# Loop to transmit test data periodically

swtch = 0
while 1:
    test = Test.confdata

# alternate between high and low values of data evry 2 seconds
    if swtch == 0:
        Test.update_high()
        swtch = not swtch
    else:
        Test.update_low()
        swtch = not swtch

# assign data to local variables
    vehicleSpd = test.vehicleSpd
    vehicleAng = test.vehicleAng
    vehicleType = test.vehicleType

    AccelPedlPos = test.AccelPedlPos
    Transmission = test.Transmission
    PowerControlStatus = test.PowerControlStatus
    IsFailure = test.IsFailure
    IsSafetyOn = test.IsSafetyOn

# send data as 2 ethernet messages
    msg1 = ["VehicleParams", vehicleSpd, vehicleAng, vehicleType]
# using pickle to encode python datatypes
    buff = pickle.dumps(msg1)
    c.send(buff)

    msg2 = ["internalParams", AccelPedlPos, Transmission, PowerControlStatus, IsFailure, IsSafetyOn]
    buff = pickle.dumps(msg2)
    c.send(buff)
# print used as mock to check transmission
    print('sent')

# disconnect server
c.close()
