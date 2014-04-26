#import RPIO as io
from RPIO import PWM

#io.setmode(io.BCM)

servo = PWM.Servo()

# Set servo on GPIO17 to 1200micros (1.2ms)
servo.set_servo(17, 1200)

# Set servo on GPIO17 to 2000micros (2.0ms)
servo.set_servo(17, 2000)

# Clear servo on GPIO17
servo.stop_servo(17)
