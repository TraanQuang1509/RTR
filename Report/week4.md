<h1 align="center"> 4TH WEEK REPORT </h1> 

## ***Intern: Tran Minh Quang***

> ### **I.**

> ### **1.1. Overview**

- A MAVLINK network is made up of systems (vehicles, ground stations, antenna trackers, etc.), which may be composed from one or more components (autopilot, camera, servos, etc.).

- Each system has a network-unique *"System ID"*, and each component has a system-unique *"Component ID"* that can be used for addressing/routing:

- The system id has a value between 1 and 255.

  - The default autopilot system id is usually 1. 

  - GCS systems and developer APIs typically use an ID at the top of the numeric range to reduce ID clashes (e.g. 255). 

- Messages can be intended for all systems, specific systems, all components in a system, or specific components within a system. The protocol defines two 8-bit fields that can (optionally) be specified in the message payload to indicate where the message should be sent/routed. If the ids are omitted or set to 0 then the message is considered a broadcast (intended for all systems/components).
  
> ### **1.2. MAVRouter**

- MAVLink Router is an application to distribute MAVLink messages between multiple endpoints (connections). It distributes packets to a single port or multiple endpoints depending on the target address. Connections can be made via UART, UDP or TCP

- Message Routing: In general, each message received on one endpoint is delivered to all endpoints in which that target system/component has been seen. If it's a broadcast message, it's delivered to all endpoints. A message is never sent back to the same endpoint it came from.

- The MAVLink organisation provides (and supports) the [mavgen](http://mavlink.io/en/getting_started/generate_libraries.html#mavgen), [mavgenerate](http://mavlink.io/en/getting_started/generate_libraries.html#mavgenerate) and [rust-mavlink](https://github.com/mavlink/rust-mavlink) tools.
