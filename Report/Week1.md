<h1 align="center"> 1ST WEEK REPORT </h1> 

## ***Intern: Tran Minh Quang***

## **I. Brushless Direct Current (BLDC) Motor**

> ### **1. Definition**

- Brushless DC motor is an electric motor that uses an electronic switching mechanism instead of using brushes and commutators as in DC motors. Therefore, the BLDC motor overcomes the phenomenon of sparking when switching in a DC motor.

- BLDC motor is a synchronous motor, this means that the rotor speed is equal to the magnetic field speed

- Brushless DC motor has only two basic parts: rotor and the stator. The rotor is the rotating part and has rotor magnets whereas stator is the stationary part and contains stator windings. In BLDC permanent magnets are attached in the rotor and move the electromagnets to the stator.
    - The stator consists of a steel core that is electrically insulated steel sheets and windings.
    - The rotor consists of a motor shaft and permanent magnets arranged alternately between the north and south poles.
<div align="center">
    <img src="https://howtomechatronics.com/wp-content/uploads/2019/02/Brushless-motor-main-parts-a-stator-and-a-rotor.png" width="500">
    
*Construction of BLDC*
</div>

> ### **2. Types of BLDC Motors**
Basically, BLDC are of two types, one is outer rotor motor and other is inner rotor motor. The basic difference between the two is only in designing, their working principles are same.

- Inner Rotor Design: the rotor is located in the centre of the motor and the stator winding surround the rotor. As the rotor is located in the core, rotor magnets do not insulate heat inside and heat get dissipated easily. Due to this reason, inner rotor designed motor produces a large amount of torque and validly used.

- Outer Rotor Design: the rotor is located in the centre of the motor and the stator winding surround the rotor. As the rotor is located in the core, rotor magnets do not insulate heat inside and heat get dissipated easily. Due to this reason, inner rotor designed motor produces a large amount of torque and validly used.

<div align="center">
    <img src="https://i.pinimg.com/originals/1d/34/09/1d340941bd00fd427fe1e7497a42be09.png" width="500">
    
*Types of BLDC Motors*
</div>


> ### **3. Working Principle**

- The working principle of the BLDC motor is based on the interaction force of the magnetic field generated by the stator and the permanent magnet on the rotor. When current flows through one of the three stator windings, it creates a magnetic pole that attracts the nearest permanent magnets with opposite poles. The rotor will continue to move if the current shifts to an adjacent winding. Sequential energization of each winding will cause the rotor to rotate in accordance with the rotating magnetic field.

<div align="center">
    <img src="https://4.bp.blogspot.com/-pJATvoj-qz8/VVQtSv0RCMI/AAAAAAAABHw/abF8cTRrEck/s1600/bldc-working.gif" width="500">
    
*Working Principle*
</div>
****
- In fact, to increase the interaction force, people will power both coils at the same time, the order of transition between the coils is controlled by the electronic circuit.

<div align="center">
    <img src="https://sklc-tinymce-2021.s3.amazonaws.com/comp/2021/03/mceclip11_1614687945.gif" width="500">
    
*Working Principle*
</div>

## **II. Electronic Speed Controller (ESC)**

- An ESC or an Electronic Speed Controller controls the brushless motor movement or speed by activating the appropriate MOSFETs to create the rotating magnetic field so that the motor rotates. The higher the frequency or the quicker the ESC goes through the 6 intervals, the higher the speed of the motor will be.

<div align="center">
    <img src="https://howtomechatronics.com/wp-content/uploads/2019/02/How-does-an-ESC-Work-Electronic-Speed-Controller-768x365.png?ezimgfmt=ng:webp/ngcb2" width="600">
    
*Electronic Speed Controller*
</div>

- However, here comes an important question, and that’s how do we know when to activate which phase. The answer is that we need to know the position of the rotor and there are two common methods used for determining the rotor position.
    - The first common method is by using Hall-effect sensors embedded in the stator, arranged equally 120 or 60 degrees from each other. As the rotors permanent magnets rotate the Hall-effect sensors sense the magnetic field and generate a logic “high” for one magnetic pole or logic “low” for the opposite pole. According to this information the ESC knows when to activate the next commutation sequence or interval.
    <div align="center">
        <img src="https://howtomechatronics.com/wp-content/uploads/2019/02/Brushless-motor-rotor-position-using-Hall-effect-sensors-768x412.png?ezimgfmt=ng:webp/ngcb2" width="700">
        
    *Hall-effect sensors*
    </div>

    - The second common method used for determining the rotor position is through sensing the back electromotive force or back EMF. The back EMF occurs as a result of the exact opposite process of generating a magnetic field or when a moving or changing magnetic field pass through a coil it induces a current in the coil. So, when the moving magnetic field of the rotor pass through the free coil, or the one that’s not active, it will induce a current flow in coil and as result a voltage drop will occur in that coil. The ESC captures these voltage drops as they occur and based on them it predicts or calculates when the next interval should take place.

    <div align="center">
        <img src="https://howtomechatronics.com/wp-content/uploads/2019/02/Back-EMF-in-Brushless-motor-768x417.png?ezimgfmt=ng:webp/ngcb2" width="700">
        
    *Back EMF*
    </div>

## **III. ESC Protocol**
> ### **1. PWM (Standard PWM)**

- PWM use a periodic input pulse of width typically between 1000uS and 2000uS for zero to full power

<div align="center">
        <img src="https://howtomechatronics.com/wp-content/uploads/2019/02/Arduino-Brushelss-Motor-Control-using-ESC.png" width="600">
        
*PWM Signal*
</div>

- Minimum rate is 50Hz corresponding to 20ms for one period

- With a pulse length of 2000uS, the maximum update rate is 500Hz, but in fact, it is only 490Hz (because there must be a break between pulses) and the default is 490Hz

- Signal delay when updating can be up to 2000us (for 490Hz)

> ### **2. OneShot** 

>> **2.1. OneShot(SyncPWM)**

- OneShot is an older protocol that uses the same pulse widths as Normal PWM but has a fixed frame rate equal to the autopilot main loop rate. 

- There is little advantage for using this protocol over regular PWM. OneShot overcomes the disadvantage of PWM, which is the delay when updating

<div align="center">
        <img src="https://oscarliang.com/ctt/uploads/2015/03/oneshot-ESC-PWM-explain.jpg" width="600">
        
*PWM & Oneshot*
</div>

>> **2.2. OneShot125 (Fast PWM)**

This protocol uses 8 times shorter pulses than PWM protocol
- With pulse length from 125us to 250us
-  It allows for 8 times faster PID control loop update rate (looptime 250us / 4kHz update rate)
- It also has 8 times shorter signal delay: only 250us instead of 2000us

>> **2.3. OneShot42 (Faster PWM)**

OneShot42 (Faster PWM) tương tự như OneShot125 nhưng nhanh gấp 3 lần (gấp 24 lần PWM)
- With pulse length from 42us to 84us
- Maximum update rate 12kHz
- Latency 84us
- 
<div align="center">
        <img src="https://1.bp.blogspot.com/-zd02VHLotwY/XrDRHpsUADI/AAAAAAAAEEo/l8LzoISs2lw9wAbdz_HgnUbbGcbDJW9LQCLcBGAsYHQ/s1600/Screen%2BShot%2B2020-05-05%2Bat%2B12.35.54%2Bpm.png" width="600">
        
*PWM, OneShot125 & OneShot42*
</div>

> ### **3. MultiShot (Fasterer PWM)** 

MultiShot is the fastest ESC protocol currently with 80x speed compared to PWM
- With pulse length from 12.5us to 25us
- Maximum update rate 40khz
- Latency 25us

### ***The above protocols all send analog signals, so they are easily affected by noise and need to be calibrated if the FC and ESC clocks are different.***
> ### **4. DShot (DigitalShot)** 

This is the "digital" protocol. It's not based on the length of a pulse but uses zeros and ones send just like over a serial port to control ESCs

DShot comes in many versions:
- DShot150: 150kbps, maximum update rate 8kHz
- DShot300: 300kbps, maximum update rate 16kHz
- DShot600: 600kbps, maximum update rate 32kHz
- DShot1200: 1200kbps, maximum update rate 64kHz

Advanatges of DShot:
- Calibration is not necessary
- Electrical noise cannot charge a throttle value
- The ESC can detect and reject throttle data corrupted by noise 
  
The DShot protocol sends a 16bits data packet from the FC to the ESC, where:
-  11 bits for throttle value (2^11 = 2048 steps) 
-  1 bit for telemetry request
-  4 bit for CRC checksum (cyclic redundancy check)

(For example DShot600 would have a frequency of 600,000/16 = 37500Hz = 37.5KHz. However, in practice, it will not as high as 37.5KHz because there needs to be some space between values)

<div align="center">
        <img src="https://oscarliang.com/ctt/uploads/2017/05/dshot1200-esc-protocol-speed-bitrate-latency.jpg" width="600">
        
*ESC protocols speed*
</div>

