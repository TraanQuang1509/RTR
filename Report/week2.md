<h1 align="center"> 2ND WEEK REPORT </h1> 

## ***Intern: Tran Minh Quang***

## **I. Unmanned Aerial vehicle (UAV) - Drone**

> ### **1. Definition**

- A drone is an unmanned aircraft. Drones are more formally known as Unmanned Aerial Vehicles (UAVs) or unmanned aircraft systems. Essentially, a drone is a flying robot that can be remotely controlled or fly autonomously using software-controlled flight plans in its embedded systems, that work in conjunction with onboard sensors and a global positioning system (GPS).


<div align="center">
    <img src="https://www.thecoronawire.com/wp-content/uploads/2021/05/BLOG_What_Types_Of_Drones_Are_There_Every_Type_Of_Drone_Explained_In_Detail_Thumbnail-1200x628.jpg" width=60%>
    
*Drone*
</div>

- UAVs were most often associated with the military. They were initially used for anti-aircraft target practice, intelligence gathering and, more controversially, as weapons platforms. Drones are now also used in a range of civilian roles, including the following:
  - Search and rescue
  - Surveillance
  - Traffic monitoring
  - Weather monitoring
  - Firefighting
  - Personal use
  - Drone-based photography
  - Videography
  - Agriculture
  - Delivery services

<div align="center">
    <img src="https://media.istockphoto.com/vectors/drone-usage-and-applications-for-commercial-and-industrial-work-vector-id1225493831" width=60%>
    
*Drone applications*
</div>

> ### **2. Common drone components**
- Frame
- Motors
- Electric Speed Controller (ESC)
- Flight control/Board
- Propellers
- Radio transmitter 
- Battery, Electronics, and Power Distribution Cables
- Camera
- Landing gear
- Fisrt person video 

> ### **3. Types of drone**

There are 4 popular types of drones
- Multi-rotor Drones: Multi-rotor drones are the easiest and cheapest option for getting an ‘eye in the sky.’ They also offer greater control over position and framing, and hence they are perfect for aerial photography and surveillance. They are called multi-rotor because they have more than one motor, more commonly tricopters (3 rotors), quadcopters (4 rotors), hexacopters (6 rotors) and octocopters (8 rotors), among others. By far, quadcopters are the most popular multi-rotor drones.

    - Pros: Accessibility, Ease of use, VTOL and hover flight, Good camera control, Can operate in a confined area
    - Cons: Short flight times, Small payload capacity
    - Technical Uses: Visual inspections, Thermal reports, Photography & Videography, 3D scans

<div align="center">
    <img src="https://www.aniwaa.com/wp-content/uploads/2019/02/drone-buying-guide-type-of-drones.jpg" width=60%>
    
*Multi-rotor Drones*
</div>

- Fixed-Wing Drones: A fixed-wing drone has one rigid wing that is designed to look and work like an aeroplane, providing the lift rather than vertical lift rotors. Hence, this drone type only needs the energy to move forward and not to hold itself in the air. This makes them energy-efficient.

  - Pros: Long-endurance flight, Large area coverage, Fast flight speed
  - Cons: Launch and recovery needs a lot of space, No VTOL/hover, Harder to fly (more training needed)
  - Technical Uses: Aerial Mapping, Inspection (Forest, Enviroment, Pineline, Power,..), 

<div align="center">
    <img src="https://3.imimg.com/data3/GC/RT/MY-1167516/fixed-wing-uav-for-aerial-mapping-and-survey-500x500.jpg" width=60%>
    
*Fixed-Wing Drones*
</div>

- Single-Rotor Drones (Helicopter): Single-rotor drone types are strong and durable. They look similar to actual helicopters in structure and design. A single-rotor has just one rotor, which is like one big spinning wing, plus a tail rotor to control direction and stability.

  - Pros: VTOL and hover flight, Long endurance (with gas power), Heavier payload capability
  - Cons: More dangerous, Harder to fly, more training needed
  - Technical Uses: Aerial LIDAR laser scan, Surveying, Carrying heavy payloads

<div align="center">
    <img src="https://image.made-in-china.com/2f0j00mJAQwKEdcguA/Save-28L-Gasoline-Engine-Power-Single-Rotor-Spraying-Drone-Agricultural-Plant-Protection-Drone-Liquid-Tank-28L-Capacity-Long-Endurance.jpg" width=70%>
    
*Fixed-Wing Drones*
</div>

- Fixed-Wing Hybrid VTOL: Hybrid VTOL drone types merge the benefits of fixed-wing and rotor-based designs. This drone type has rotors attached to the fixed wings, allowing it to hover and take off and land vertically. This new category of hybrids are only a few on the market, but as technology advances, this option can be much more popular in the coming years.

  - Pros: VTOL, Long-endurance flight
  - Cons: Not perfect at either hovering or forward flight, Still in development
  - Technical Uses: Drone Delivery

<div align="center">
    <img src="https://www.suasnews.com/wp-content/uploads/2016/06/jouav-cw10.jpg" width=60%>
    
*Fixed-Wing Hybrid VTOL Drones*
</div>

## **II. Aerodynamics: The Theory of Lift**

- The incorrect theories all try to apply either Bernoulli's principle or Newton's Third Law, however they make errors and assumptions that do not correspond with the nature of aerodynamics.

- Bernoulli's equation explains that due to the fact that air molecules are not closely bound together, they are able to flow and move freely around an object. Since the molecules themselves have a velocity associated with them, and the velocity can change depending on where the molecules are with respect to the object, the pressure changes as well.
  
<div align="center">
    <img src="https://images.saymedia-content.com/.image/c_limit%2Ccs_srgb%2Cq_auto:eco%2Cw_585/MTc0NjQ2NDA0OTQ0NTA0NTkx/aerodynamics-the-theory-of-lift.webp" width=50%>
    
*Bernoulli's Principle*
</div>

- The air molecules closest to the top surface of the aerofoil are kept close to the surface due to there being higher pressure at the top of the particles as opposed to the bottom of them, supplying the centrifugal force. The high pressure above the particles pushes them towards the aerofoil, which is why they stay attached to the curved surface instead of continuing on a straight path. This is known as the Coanda effect, and acts on the airflow on the lower surface of the aerofoil in the same way. The curved deflection of the air molecules creates a low pressure above the aerofoil and a high pressure below the aerofoil, and this difference in pressure generates the lift.

<div align="center">
    <img src="https://images.saymedia-content.com/.image/c_limit%2Ccs_srgb%2Cq_auto:eco%2Cw_588/MTc0NjQ2NDA0OTQ0MjQyNDQ3/aerodynamics-the-theory-of-lift.webp" width=50%>
    
*Newton's Third Law of Motion*
</div>

- Newton's Third Law states that every force has an equal and opposite reaction force. In the case of an aerofoil, the air flow is being forced downwards by the Coanda effect, deflecting the flow. So the air molecules should be pushing the aerofoil in the opposite direction with equal magnitude, and that reaction force is lift.

> ### **III. Working principle of Quadcopter**

- There are many popular types of quadcopter and generally have two rotors spinning clockwise and two counterclockwise (CCW). Flight control is provided by independent variation of the speed and hence lift and torque of each rotor. Pitch and roll are controlled by varying the net centre of thrust, with yaw controlled by varying the net torque.

<div align="center">
    <img src="https://thumbs.dreamstime.com/z/motor-order-diagrams-quad-drone-quadcopter-set-vector-infographics-airframes-types-h-v-p-136590187.jpg" width="60%" >

*Types of Quadcopter*
</div>

- **Climb Ascend** – By increasing the thrust (speed) of the four quadcopter rotors so that the upward force is greater than the weight and pull of gravity.

- **Hover Still** – To hover, the net thrust of the four rotors push the drone up and must be exactly equal to the gravitational force pulling it down.

- **Climb Ascend** – By increasing the thrust (speed) of the four quadcopter rotors so that the upward force is greater than the weight and pull of gravity.

<div align="center">
    <img src="https://cfdflowengineering.com/wp-content/uploads/2020/09/word-image-36.png" width="60%" >

*Working principle of Quadcopter*
</div>

- **Yaw** -A quadcopter adjusts its yaw by applying more thrust to rotors rotating in one direction. 

- **Pitch and Roll** - A quadcopter adjusts its pitch or roll by applying more thrust to one rotor (or two adjacent rotors) and less thrust to the diametrically opposite rotor.

<div align="center">
    <img src="https://cfdflowengineering.com/wp-content/uploads/2020/09/word-image-37.png" width="60%" >

*Working principle of Quadcopter*
</div>

> ### **IV. Serial Communication Protocols**

> ### **1. SPI**

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

> ### **2. I2C**

- I2C means inter-integrated–circuit. This protocol is ideal for modules and sensors. I2C is a bidirectional synchronous serial bus.  It needs two wires for data transmission between devices linked to the bus.

- I2C protocol is ideal for applications that require various parts. 12C can have several masters and slaves

- This protocol features two pins. These pins are the Serial Clock Line (SCL) pin and the Serial Data Line (SDL) pin. The SDL transfers and receives data. Meanwhile, the SCL functions as a clock. The master controls the clock bus.

- I2C protocol connects low-speed, short-distance peripherals on circuit boards. This protocol is commonly used in reading hardware sensors and reading memory

<div align="center">
    <img src="https://i.stack.imgur.com/B2O63.png" width="40%" height="400px">
    <img src="https://deviot.vn/storage/deviot/Giao%20tiep%20SPI%207.png" width="40%" height="400px">
    

*Serial Peripheral Interface - SPI*
</div>

