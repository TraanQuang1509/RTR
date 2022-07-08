<h1 align="center"> BÁO CÁO TUẦN 1 </h1> 

## ***Thực tập sinh: Trần Minh Quang***

## **I. Động cơ không chổi than**

> ### **1. Định nghĩa**

- Động cơ một chiều không chổi than (Brushless Direct Current- BLDC) là động cơ điện sử dụng cơ chế chuyển mạch bằng điện tử thay vì sử dụng chổi than và cổ góp như ở động cơ điện một chiều. Do đó động cơ BLDC khắc phục được hiện tượng tia lửa điện khi chuyển mạch ở động cơ một chiều.

- BLDC motor là động cơ đồng bộ, điều này có nghĩa là tốc độ roto bằng với tốc độ từ trường

> ### **2. Cấu tạo**

>> **2.1.Stator**

- Phân loại BLDC motor theo stato có 3 loại: một pha, hai pha và ba pha. Trong đó động cơ ba pha được sử dụng rộng rãi nhất.

![Cấu tạo BLDC](https://kienthuctudonghoa.com/wp-content/uploads/2020/10/dong-co-BLDC-3.jpg "Cấu tạo BLDC")

<img src="https://kienthuctudonghoa.com/wp-content/uploads/2020/10/dong-co-BLDC-3.jpg" alt="Smiley face" width="300" height="250" style="text-align:center;">

- Stato bao gồm lõi thép là các lá thép kỹ thuật điện ghép cách điện với nhau và dây quấn.

- Hình dạng suất điện động của BLDC motor có thể là hình sin hoặc hình thang, tùy theo cách quấn dây và khe hở không khí. Động cơ có suất điện động hình sin tạo ra moment mượt mà hơn động cơ hình thang, mặc dù chi phí cao hơn do chúng sử dụng thêm các cuộn dây đồng.

>> **2.2.Rotor**

- Roto bao gồm trục đông cơ và các nam châm vĩnh cửu được bối trí xen kẽ giữa các cực bắc và nam.

- Có 2 loại rotor: rotor đặt trong và rotor đặt ngoài. Rotor đặt ngoài phổ biến hơn vì nó có momen xoắn lớn hơn

![Rotor](https://i.pinimg.com/originals/1d/34/09/1d340941bd00fd427fe1e7497a42be09.png "rotor")

> ### **3. Nguyên lý hoạt động**

- Nguyên lý hoạt động của động cơ BLDC dựa trên lực tương tác của từ trường do stato tạo ra và nam châm vĩnh cửu trên roto. Khi dòng điện chạy qua một trong ba cuộn dây stato sẽ tạo ra cực từ hút các nam châm vĩnh cửu gần nhất có cực từ trái dấu. Roto sẽ tiếp tục chuyển động nếu dòng điện dịch chuyển sang một cuộn dây liền kề. Cấp điện tuần tự cho mỗi cuộn dây sẽ làm cho roto quay theo từ trường quay.
  
![nguyên lý hoạt động](https://kienthuctudonghoa.com/wp-content/uploads/2020/10/dong-co-BLDC-9.jpg)

- Trong thực tế để tăng lực tương tác người ta sẽ cấp điện cùng lúc cả hai cuộn dây, thứ tự chuyển tiếp giữa các cuộn dây được điều khiển bởi mạch điện tử.

![](https://kienthuctudonghoa.com/wp-content/uploads/2020/10/dong-co-BLDC-14.png)

## **II. Electronic Speed Controller (ESC)**

- Một ESC điều khiển chuyển động hoặc tốc độ của động cơ không chổi than bằng cách kích hoạt các MOSFETs thích hợp để tạo từ trường quay để động cơ quay. Tần số càng cao tốc độ của động cơ sẽ càng cao.

![](https://howtomechatronics.com/wp-content/uploads/2019/02/How-does-an-ESC-Work-Electronic-Speed-Controller-768x365.png?ezimgfmt=ng:webp/ngcb2)

- Tuy nhiên, ta cần phải biết khi nào thì cần kích hoạt các MOSFETs. Có 2 cách phổ biến là: sử dụng cảm biến vị trí hiệu ứng Hall (gọi tắt là cảm biến Hall) và đo dòng điện cảm ứng (back EMF)
    - Cảm biến Hall được gắn trên stato của BLDC để phát hiện các nam châm vĩnh cửu trên roto khi quét qua nó. Các cảm biến Hall có thể được gắn để tạo tín hiệu phản hồi lệch pha nhau 600 hay 1200 điện. Khi các nam châm vĩnh cửu quay, các cảm biến hiệu ứng Hall cảm nhận được từ trường và tạo ra logic "cao" cho một cực từ hoặc logic "thấp" cho cực đối diện. Theo thông tin này, ESC biết khi nào sẽ kích hoạt chuỗi hoặc khoảng thời gian giao tiếp tiếp theo.
  
    ![Cảm biến Hall](https://howtomechatronics.com/wp-content/uploads/2019/02/Brushless-motor-rotor-position-using-Hall-effect-sensors-768x412.png?ezimgfmt=ng:webp/ngcb2 "Cảm biến Hall")

    - Phương pháp phổ biến thứ hai được sử dụng để xác định vị trí rotor là thông qua việc đo lực điện động trở về hoặc EMF . EMF phía sau xảy ra là kết quả của quá trình hoàn toàn ngược lại để tạo ra từ trường hoặc khi một từ trường di chuyển hoặc thay đổi đi qua một cuộn dây, nó tạo ra một dòng điện trong cuộn dây. Vì vậy, khi từ trường di chuyển của rotor đi qua cuộn dây, nó sẽ tạo ra một dòng điện cảm ứng trong cuộn dây và kết quả là sự sụt giảm điện áp sẽ xảy ra trong cuộn dây đó. ESC thu được các điện áp này khi chúng xảy ra và dựa trên chúng, nó dự đoán hoặc tính toán khi nào sẽ diễn ra khoảng tiếp theo.
    
    ![](https://howtomechatronics.com/wp-content/uploads/2019/02/Back-EMF-in-Brushless-motor-768x417.png?ezimgfmt=ng:webp/ngcb2)

## **III. ESC Protocol**
> ### **1. PWM (Standard PWM)**

- PWM sử dụng xung đầu vào có chu kì cố định với duty cycle từ 1000uS đến 2000uS tương ứng với mức năng lượng tối thiểu vào tối đa

![PWM Signal](https://howtomechatronics.com/wp-content/uploads/2019/02/Arduino-Brushelss-Motor-Control-using-ESC.png "PWM Signal")

- Tốc độ nhỏ nhất là 50Hz tương ứng với 20ms cho một chu kì 

- Với duty cycle là 2000uS thì tốc độ update tối đa là 500Hz, tuy nhiên trên thực tế chỉ là 490Hz (vì giữa các xung phải có khoảng nghỉ) và mặc định là 490Hz

- Tín hiệu delay khi update có thể lên đến 2000us (đối với 490Hz) 

> ### **2. OneShot** 

>> **2.1. OneShot(SyncPWM)**
- Oneshot  là một giao thức cũ hơn, cũng sử  dụng độ rộng xung giống như PWM nhưng chu kỳ bằng với thời gian của 1 PID loop

- OneShot khắc phục được nhược điểm của PWM là độ trễ khi update

![PWM & Oneshot](https://oscarliang.com/ctt/uploads/2015/03/oneshot-ESC-PWM-explain.jpg "PWM & Oneshot")

>> **2.2. OneShot125 (Fast PWM)**

OneShot125  sử dụng xung ngắn hơn 8 lần so với PWM
- Với độ rộng xung từ 125us - 250us
- Cho phép tốc độ update nhanh gấp 8 lần (tối đa 4kHz)
- Giảm delay gấp 8 lần so với PWM (250us Vs. 20000us)

>> **2.3. OneShot42 (Faster PWM)**

OneShot42 (Faster PWM) tương tự như OneShot125 nhưng nhanh gấp 3 lần (gấp 24 lần PWM)
- Với độ rộng xung từ 125us - 250us
- Tốc độ update tối đa 12kHz
- Độ trễ 84us

![PWM, OneShot125 & OneShot42](https://1.bp.blogspot.com/-zd02VHLotwY/XrDRHpsUADI/AAAAAAAAEEo/l8LzoISs2lw9wAbdz_HgnUbbGcbDJW9LQCLcBGAsYHQ/s1600/Screen%2BShot%2B2020-05-05%2Bat%2B12.35.54%2Bpm.png "PWM, OneShot125 & OneShot42")

> ### **3. MultiShot (Fasterer PWM)** 

MultiShot là ESC protocol nhanh nhất hiện tại với tốc độ gấp 80 lần so với PWM
- Với độ rộng xung từ 12.5us - 25us
- Tốc độ update tối đa lên tới 40khz
- Độ trễ  25us

### ***Các giao thứ trên đều gửi tín hiệu analog nên dễ bị ảnh hưởng bởi nhiễu và phải cần hiệu chỉnh nếu xung clock của FC và ESC khác nhau***
> ### **4. DShot (DigitalShot)** 

DShot dùng tín hiệu digital để truyền tính hiệu từ FC tới ESC

Có 4 tốc độ cho DShot:
- DShot150: 150kbps, tốc độ update tối đa 8kHz
- DShot300: 300kbps, tốc độ update tối đa 16kHz
- DShot600: 600kbps, tốc độ update tối đa 32kHz
- DShot1200: 1200kbps, tốc độ update tối đa 64kHz

DShot protocol sẽ gửi một data packet 16bits từ FC xuống ESC, trong đó:
- 11 bits cho giá trị đầu ra của PID (với resolution là 2^11 = 2048 steps)
- 1 bit cho telemetry request
- 4 bits cho RCR checksum (cyclic redundancy check)

(Ví dụ với Dshot600, 600000/16 = 37500Hz = 37,5kHz. Tuy nhiên trên thực tế sẽ không cao bằng 37.5kHz bởi vì cần có khoảng cách giữ các giá trị)

![ESC protocol speed](https://oscarliang.com/ctt/uploads/2017/05/dshot1200-esc-protocol-speed-bitrate-latency.jpg "ESC protocol speed")

Ưu điểm của DShot:
- Không cần hiệu chỉnh
- Giá trị không bị thay đổi bởi nhiễu 
- ESC có thể nhận biết là loại bỏ giá trị sai