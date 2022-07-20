<h1 align="center"> 3RD WEEK REPORT </h1> 

## ***Intern: Tran Minh Quang***

> ### **IV. Serial Communication Protocols**

> ### **4.1. SPI**

- The SPI means Serial Peripheral Interface. The serial peripheral interface is specifically designed for the connection of microcontrollers. This interface functions at full-duplex and operates at faster data transmission rates

- The SPI interface makes use of the master-to-slave format to regulate several slave devices with a master. SPI utilizes a built-in clock from the master. This helps to ensure the slave and master devices are operating on the same frequency. SPI is commonly used in SD cards and display modules.

- It uses four wires which are:

    - MISO (Master Out Slave)
    - SS/CS (Chip Select)
    - SCK (Serial Clock Line)
    - MOSI (Master In Slave Out)

<div align="center">
    <img src="https://dammedientu.vn/wp-content/uploads/2019/05/SPI_Master_three_slaves.png" width="60%">
    <img src="https://deviot.vn/storage/deviot/Giao%20tiep%20SPI%207.png" width="60%">
    

*Serial Peripheral Interface - SPI*
</div>

- SPI communicates in two different ways.  Firstly, it selects every device with a CS line. Each device needs a separate CS line. The second method involves daisy chaining. Here, every device is connected to another via its data out to the data in line. The number of SPI devices you can connect has no limit.

- Pros

    - Supports full-duplex
    - Utilizes a master’s clock. So, it doesn’t require precision oscillators in slaves
    - Faster data transmission rate
    - Features simple software implementation
    - Has no stop and start bits
    - Features no complex slave addressing system

- Cons
    - There will be complex wiring when more than one slave is in communication
    - Utilizes four wires
    - Doesn’t acknowledge data receiving
    - Doesn’t check errors
    - It gives room for a single master

> ### **4.2. I2C**

- I2C means inter-integrated–circuit. This protocol is ideal for modules and sensors. I2C is a bidirectional synchronous serial bus.  It needs two wires for data transmission between devices linked to the bus.

- I2C protocol is ideal for applications that require various parts. 12C can have several masters and slaves

- This protocol features two pins. These pins are the Serial Clock Line (SCL) pin and the Serial Data Line (SDL) pin. The SDL transfers and receives data. Meanwhile, the SCL functions as a clock. The master controls the clock bus.

- I2C protocol connects low-speed, short-distance peripherals on circuit boards. This protocol is commonly used in reading hardware sensors and reading memory

<div align="center">
    <img src="https://i.stack.imgur.com/B2O63.png" width="60%">
    <img src="https://prodigytechno.com/wp-content/uploads/2022/04/Data-Transfer-on-I2C-bus-1-1024x249.png" width="80%">
    

*Serial Peripheral Interface - SPI*
</div>

> ### **4.3. UART**

- A UART refers to Universal Asynchronous Receiver Transmitter. It is a form of device-to-device digital communication.

- It is a protocol used for full-duplex serial communication. The UART is a chip designed to carry out asynchronous communication.

- The UART features two core components; the receiver and transmitter. The receiver has a control logic, receiver shift register, and a receive hold register. The transmitter features the control logic, transmit hold register, and transmit shift.

- For data transmission to occur, the receiver and the transmitter must agree with some configurations. These are:
    - Start bit
    - Baud speed (4800, 9600, 19200,..., 115200)
    - Parity bit
    - Stop bit
    - Data length

<div align="center">
    <img src="https://www.circuitbasics.com/wp-content/uploads/2016/01/Introduction-to-UART-Basic-Connection-Diagram.png" width="60%">
    <img src="https://developer.electricimp.com/sites/default/files/attachments/images/uart/uart3.png" width="60%">
    
    

*Universal Asynchronous Receiver Transmitter - UART*
</div>

- Pros
    - It doesn’t need any clock
    - UART is very easy to operate
    - Features parity bit that enables error checking
    - Uses two wires
- Cons
    - The data frame size is limited to 9 bits
    - Features low data transmission speeds
    - UART can’t use several master systems and slaves

> ### **4.3. CANBus**

- The Controller Area Network - CAN bus is a message-based protocol designed to allow the Electronic Control Units (ECUs) found in today’s automobiles, as well as other devices, to communicate with each other in a reliable, priority-driven fashion. Messages or “frames” are received by all devices in the network, which does not require a host computer.

- In 1986, Bosch introduced the CAN standard at the SAE Congress in Detroit. One year later Intel Corporation began shipments of the first CAN controller chips, and the automotive world was changed forever

- Devices on a CAN bus are called “nodes.” Each node consists of a CPU, CAN controller, and a transceiver, which adapts the signal levels of both data sent and received by the node. All nodes can send and receive data, but not at the same time. All nodes are connected to each other through a two wire bus.

<div align="center">
    <img src="https://capgemini-engineering.com/as-content/uploads/sites/7/2021/11/two-wired-communication-between-nodes.png" width="60%">

*Genenal layout of a CAN bus*
</div>

- Nodes cannot send data directly to each other. Instead, they send their data onto the network, where it is available to any node to which it has been addressed. The CAN protocol is lossless, employing a bitwise arbitration method to resolve contentions on the bus. 

- With CAN, all data are sent in frames. There are two variants of the message length: standard and extended. The real difference is the additional 18-bit identifier in the arbitration field.

- Advantages of CAN bus: Simple and Low Cost, Fully Centralized, Extremely Robust, Efficient, Reduced Vehicle Weight, Easy Deployment, Resistant to EMI (Electromagnetic Induction)

- Popular CAN Bus Applications: motorcycles, automobiles, trucks, Ships, Airplanes, Elevators,...
<div align="center">
    <img src="https://dewesoft.com/upload/news/daq/can-bus/can-data-message-structure.png" width="70%"> 
    <img src="https://i.stack.imgur.com/O00QY.png" width="70%"> 


*Standard and Extended frame of the CAN data message architecture*
</div>

- Variations of the CAN Bus:
  - Low Speed CAN
  - High Speed CAN
  - CAN FD (Flexible Data Rate CAN)

> ### **4.3. MAVlink**

- MAVLink is a serial protocol most commonly used to send data and commands between vehicles and ground stations (and between onboard drone components)

<div align="center">
    <img src="https://ardupilot.org/dev/_images/mavlink-message-flow.png" width="60%"> 


*MAVlink Protocol*
</div>

- The protocol defines a large set of messages 

- MAVLink messages can be sent over almost any serial connection and does not depend upon the underlying technology (wifi, 900mhz radio, etc)

- The messages are not guaranteed to be delivered which means ground stations or companion computers must often check the state of the vehicle to determine if a command has been executed

<div align="center">
    <img src="https://ardupilot.org/dev/_images/mavlink-frame.png" width="60%"> 


*Message Format of MAVlink*
</div>

- Messages are no more than 263 bytes

- The sender always fills in the *"System ID"* and *"Component ID"* fields so that the receiver knows where the packet came from.

  - The *"System ID"* is a unique ID for each vehicle or ground station. Ground stations normally use a high system id like “255” and vehicles default to use “1”
  - The *"Component ID"* for the ground station or flight controller is normally “1”
  -  Other MAVLink capable device on the vehicle (i.e. companion computer, gimbal) should use the same *"System ID"* as the flight controller but use a different *"Component ID"*

- The Data portion of the message holds the individual field values being sent