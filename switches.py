import time
import RPi.GPIO as io

io.setmode(io.BCM)

pir_pin = 18
door_pin = 23

io.setup(pir_pin, io.IN)
io.setup(door_pin, io.IN, pull_up_down=io.PUD_UP)

count = 0;

while True:
	if io.input(pir_pin):
		count += 1;
		print("PIR ALARM (" + str(count) + ")! ")

	if io.input(door_pin):
		print("DOOR ALARM!")
	
	time.sleep(0.5)

