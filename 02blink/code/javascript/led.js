// 导入 rpio 包
var GPIO = require('rpio');

// 声明11号口是用于输出模式
GPIO.open(11, GPIO.OUTPUT, GPIO.LOW);

// 设置11号口为高电压，也就是11号口变为3.3伏
// 这行代码执行之后，11号口变为高电压，
// 那么根据电路原理，led灯就会亮起来
GPIO.write(11, GPIO.HIGH);

// 程序休眠3秒钟，程序休眠期间，led灯会一直亮着
GPIO.sleep(3);

// 设置11号口为低电压，也就是11号口变为0伏，和GND一样
// 这行代码执行之后，11号口变为低电压，那么根据电路原理，led灯就会熄灭
GPIO.write(11, GPIO.LOW);
