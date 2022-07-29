<h1 align="center"> 4TH WEEK REPORT </h1> 

## ***Intern: Tran Minh Quang***

> ### **MAVRouter**

> ### **1. Overview**

- A MAVLINK network is made up of systems (vehicles, ground stations, antenna trackers, etc.), which may be composed from one or more components (autopilot, camera, servos, etc.).

- Each system has a network-unique *"System ID"*, and each component has a system-unique *"Component ID"* that can be used for addressing/routing:

- The system id has a value between 1 and 255.

  - The default autopilot system id is usually 1. 

  - GCS systems and developer APIs typically use an ID at the top of the numeric range to reduce ID clashes (e.g. 255). 

- Messages can be intended for all systems, specific systems, all components in a system, or specific components within a system. The protocol defines two 8-bit fields that can (optionally) be specified in the message payload to indicate where the message should be sent/routed. If the ids are omitted or set to 0 then the message is considered a broadcast (intended for all systems/components).
  
> ### **2. MAVRouter**

- MAVLink Router is an application to distribute MAVLink messages between multiple endpoints (connections). It distributes packets to a single port or multiple endpoints depending on the target address. Connections can be made via UART, UDP or TCP

- Message Routing: In general, each message received on one endpoint is delivered to all endpoints in which that target system/component has been seen. If it's a broadcast message, it's delivered to all endpoints. A message is never sent back to the same endpoint it came from.

- The MAVLink organisation provides (and supports) the [mavgen](http://mavlink.io/en/getting_started/generate_libraries.html#mavgen), [mavgenerate](http://mavlink.io/en/getting_started/generate_libraries.html#mavgenerate) and [rust-mavlink](https://github.com/mavlink/rust-mavlink) tools.

  - Mavgen: [C](http://mavlink.io/en/mavgen_c/), [Python (Pymavlink)](http://mavlink.io/en/mavgen_python/), C++11, C-Sharp, Java, JavaScript, Lua, Objective C, Swift
  - Pymavlink: is a low level and general purpose MAVLink message processing library, written in Python. It has been used to implement MAVLink communications in many types of MAVLink systems, including a GCS (MAVProxy), Developer APIs (DroneKit) and numerous companion computer MAVLink applications.

> ### **3. Some basic Mission Commands**

- MAVLink commands ([MAV_CMD](https://mavlink.io/en/messages/common.html#MAV_CMD)) and messages are different! These commands define the values of up to 7 parameters that are packaged INSIDE specific messages used in the Mission Protocol and Command Protocol. Use commands for actions in missions or if you need acknowledgment and/or retry logic from a request. 

  - **MAV_CMD_COMPONENT_ARM_DISARM**: The command supports disarming on the ground and in flight (The motors will disarm automatically after landing) 
    - Param1: 1 to arm, 0 to disarm (only on the ground).
    - Param2: A value of 21196 will disarm the vehicle in flight.
    - See example in Pymavlink  [here](https://github.com/TraanQuang1509/RTR/blob/main/Report/Mavlink%20example/arm.py)

  - **MAV_CMD_NAV_TAKEOFF**: The vehicle will climb straight up from it’s current location to the specified altitude. If the mission is begun while the copter is already flying, the vehicle will climb straight up to the specified altitude, if the vehicle is already above the altitude the command will be ignored and the mission will move onto the next command immediately.
    - Param7: Altitude(m)
    - See example in Pymavlink [here](https://github.com/TraanQuang1509/RTR/blob/main/Report/Mavlink%20example/takeoff.py)

  - **MAV_CMD_NAV_LAND**: The copter will land at its current location or proceed at current altitude to the lat/lon coordinates provided (if non-zero) and land. This is the mission equivalent of the [LAND flight mode](https://ardupilot.org/copter/docs/land-mode.html#land-mode).
    - Param5: Target latitude(If zero, the Copter will land at the current latitude).
    - Param6: Longitude (If zero, the Copter will land at the current longitude).
    - See example in Pymavlink [here](https://github.com/TraanQuang1509/RTR/blob/main/Report/Mavlink%20example/land.py)

  - **MAV_CMD_NAV_RETURN_TO_LAUNCH**: Copter return to the home location and then land. The home location is where the vehicle was last armed (or when it first gets GPS lock after arming if the vehicle configuration allows this).
    - The parameters are all ignored.
    - See example in Pymavlink [here](https://github.com/TraanQuang1509/RTR/blob/main/Report/Mavlink%20example/home.py)

  - **Movement Command**: These commands can be used to control the vehicle’s position, velocity or attitude while in [Guided Mode](https://ardupilot.org/copter/docs/ac2_guidedmode.html#ac2-guidedmode)
    - **SET_POSITION_TARGET_LOCAL_NED**: Sets a desired vehicle position in a local north-east-down coordinate frame. Used by an external controller to command the vehicle (manual controller or other system).
    - **SET_POSITION_TARGET_GLOBAL_INT**: Sets a desired vehicle position, velocity, and/or acceleration in a global coordinate system (WGS84). Used by an external controller to command the vehicle (manual controller or other system).
    - See example in Pymavlink [here](https://github.com/TraanQuang1509/RTR/blob/main/Report/Mavlink%20example/move.py)

  - **MAV_CMD_DO_CHANGE_SPEED**: Sets the desired maximum speed in meters/second (only). Both the speed-type and throttle settings are ignored.
    - Param2: Target speed (m/s).
    - See example in Pymavlink [here](https://github.com/TraanQuang1509/RTR/blob/main/Report/Mavlink%20example/speed.py)

  - **MAV_CMD_MISSION_START**: This command can be used to start a mission when the Copter is on the ground in AUTO mode. If the vehicle is already in the air then the mission will start as soon as you switch into AUTO mode (so this command is not needed/ignored). This allows a GCS/companion computer to start a mission in AUTO without raising the throttle.
    - The parameters are all ignored.
    - See example in Pymavlink [here](https://github.com/TraanQuang1509/RTR/blob/main/Report/Mavlink%20example/mission.py)

[Simulate Quadcopter by MissionPlanner using Pymavlink](https://www.youtube.com/watch?v=ljK1sFfUoeU)