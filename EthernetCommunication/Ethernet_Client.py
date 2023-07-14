import pickle
import socket
import can
import canBUS


# take the server name and port name

host = 'local host'
port = 5000

# create a socket at client side
# using TCP / IP protocol
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

# connect it to server and port
# number on local computer.
s.connect(('127.0.0.3', port))

# receive message string from
# server, at a time 1024 B
msg = s.recv(1024)

# repeat as long as message
# string are not empty
while msg:

    msg = s.recv(1024)
    try:
        msg = pickle.loads(msg)
        buffer = []
        for i in range(1, len(msg)):
            if isinstance(msg[i], str):
                temp = ord(msg[i])
            else:
                temp = msg[i]
            buffer.append(temp)

        if msg[0] == "VehicleParams":
            Rx_VehicleSpeed = buffer[0]
            Rx_VehicleAngle = buffer[1]
            Rx_VehicleType = buffer[2]
            msg1 = can.Message(
                arbitration_id=0xabcde, data=buffer)
        elif msg[0] == "internalParams":
            Rx_AccelPedlPos = buffer[0]
            Rx_Transmission = buffer[1]
            Rx_PowerControlStatus = buffer[2]
            Rx_IsFailure = buffer[3]
            Rx_IsSafetyOn = buffer[4]
            msg1 = can.Message(
                arbitration_id=0xabcdf, data=buffer)

        canBUS.bus1.send(msg1)
        msg2 = canBUS.bus2.recv()
#        canBuffer = [msg2.data[0]]

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



    except:
        print("exception")

# disconnect the client
s.close()
