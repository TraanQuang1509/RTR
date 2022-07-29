from pymavlink import mavutil

# Start a connection listening to a UDP port
the_connection = mavutil.mavlink_connection('udpin:localhost:14551')

# Wait for the first heartbeat
#   This sets the system and component ID of remote system for the link
the_connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" %
      (the_connection.target_system, the_connection.target_component))

# param5:latitude(0=current) param6:longitude
the_connection.mav.command_long_send(the_connection.target_system, the_connection.target_component,
                                     mavutil.mavlink.MAV_CMD_NAV_RETURN_TO_LAUNCH, 0, 0, 0, 0, 0, 0, 0, 0)

msg = the_connection.recv_match(type='COMMAND_ACK', blocking=True)
print(msg)

# Set yaw angle param1:angle(deg) param2:speed(deg/s) #param4:abs(0)/rel(1) param3:CW(1)/CCW(0)
the_connection.mav.command_long_send(the_connection.target_system, the_connection.target_component,
                                     mavutil.mavlink.MAV_CMD_CONDITION_YAW, 0, 0, 25, 0, 0, 0, 0, 0) #param4 = 0, absolute angle

msg = the_connection.recv_match(type='COMMAND_ACK', blocking=True)
print(msg)
      