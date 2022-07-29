from pymavlink import mavutil
import time
# Start a connection listening to a UDP port
the_connection = mavutil.mavlink_connection('udpin:localhost:14551')

# Wait for the first heartbeat
# This sets the system and component ID of remote system for the link
the_connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" %
      (the_connection.target_system, the_connection.target_component))

# Move to position relative to home position (local coordinate)
the_connection.mav.send(mavutil.mavlink.MAVLink_set_position_target_local_ned_message(10, the_connection.target_system,
                        the_connection.target_component, mavutil.mavlink.MAV_FRAME_LOCAL_NED, int(0b110111111000), 100, -100, -10, 0, 0, 0, 0, 0, 0, 0, 0)) 
                                                                                                                #100m to the North, 100m to the West at Altitude 10m
# msg = the_connection.recv_match(type='COMMAND_ACK', blocking=True)
# print(msg)

# Move to position move to specified latitude and longitude (Global coordinate)
# the_connection.mav.send(mavutil.mavlink.MAVLink_set_position_target_global_int_message(10, the_connection.target_system,
#                         the_connection.target_component, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, int(0b110111111000), int(-35.3635935 * 10 ** 7), int(149.1645098 * 10 ** 7), 10, 0, 0, 0, 0, 0, 0, 0, 0))
                                                                                                                                # At Latitude 
# msg = the_connection.recv_match(type='COMMAND_ACK', blocking=True)
# print(msg)

# Set yaw angle param1:angle(deg) param2:speed(deg/s) #param4:abs(0)/rel(1) param3:CW(1)/CCW(0)
the_connection.mav.command_long_send(the_connection.target_system, the_connection.target_component,
                                     mavutil.mavlink.MAV_CMD_CONDITION_YAW, 0, 0, 25, 0, 0, 0, 0, 0) #param4 = 0, absolute angle
msg = the_connection.recv_match(type='COMMAND_ACK', blocking=True)
print(msg)

# Monitor Current position of the Copter while moving
while 1:
    msg = the_connection.recv_match(
        type='LOCAL_POSITION_NED', blocking=True)
    print(msg)
    time.sleep(1)
