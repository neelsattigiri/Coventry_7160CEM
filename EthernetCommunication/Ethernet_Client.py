import pickle
import socket
import can
import canBUS


# take the server name and port name

host = 'local host'
port = 5000

# create a socket for client
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

# connect socket to a port on local machine
s.connect(('127.0.0.3', port))

# receive message as a string from the server
msg = s.recv(1024)

# loop till message is not received

while msg:

    msg = s.recv(1024)
    # try to load the data using pickle
    try:
        msg = pickle.loads(msg)
        # a buffer is used between ethernet and CAN
        # buffer is used to convert to ASCII if input is a char
        buffer = []
        for i in range(1, len(msg)):
            if isinstance(msg[i], str):
                temp = ord(msg[i])
            else:
                temp = msg[i]
            buffer.append(temp)

        # Separate into 2 CAN messages based on ID at first index
        if msg[0] == "VehicleParams":
            Rx_VehicleSpeed = buffer[0]
            Rx_VehicleAngle = buffer[1]
            Rx_VehicleType = buffer[2]
            msg1 = can.Message(
                arbitration_id=0xabcde, data=buffer)
        # different arbitration id used to separate CAN messages
        elif msg[0] == "internalParams":
            Rx_AccelPedlPos = buffer[0]
            Rx_Transmission = buffer[1]
            Rx_PowerControlStatus = buffer[2]
            Rx_IsFailure = buffer[3]
            Rx_IsSafetyOn = buffer[4]
            msg1 = can.Message(
                arbitration_id=0xabcdf, data=buffer)

        # send data to can bus
        canBUS.bus1.send(msg1)

        # receive data from can bus
        msg2 = canBUS.bus2.recv()

        # identify message using arbitration_id - acts like a CANdb
        # Plan to implement as a separate library
        if msg2.arbitration_id == 0xabcde:
            print('Speed=', msg2.data[0])
            print('Angle=', msg2.data[1])
            print('Type=', chr(msg2.data[2]))
            print("------------------------------")

        elif msg2.arbitration_id == 0xabcdf:
            print('AccelPedlPos=', msg2.data[0])
            print('Transmission=', msg2.data[1])
            print('PowerControlStatus=', msg2.data[2])
            print('IsFailure=', msg2.data[3])
            print('IsSafetyOn=', msg2.data[4])
            print("---------------------------------------------------------")
            print("---------------------------------------------------------") 


    # print exception message if an exception occurs
    except:
        print("exception")

# disconnect the client
s.close()
