import RPIO as io

def callback(gpio_id, val):
	if gpio_id == 18:
		if val:
			print "START"
		else:
			print "STOP"



	

io.setup(18, io.IN)

io.add_interrupt_callback(18, callback)

io.wait_for_interrupts()
