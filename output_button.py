import RPi.GPIO as io

io.setmode(io.BCM)
io.setup(25, io.IN)

while True:
	input_value = io.input(25)
	if input_value == False:
		print("The button has been pressed")
		while input_value == False:
			input_value = io.input(25)

