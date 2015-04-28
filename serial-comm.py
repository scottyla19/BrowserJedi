import serial #Import Serial Library
import os



arduinoSerialData = serial.Serial('/dev/cu.usbmodem411',9600) #Create Serial port object called arduinoSerialData
def press_key_command(data):
	print data
	action = ''
	if "=" in data:
		action = data.split("=")[1].strip()

	actions = {"Left Swipe":"(ASCII character 8)",
				"Up Swipe":['"+"', "{command down}"],
				"Right Swipe":["(ASCII character 8)","{shift down}"],
				"Down Swipe":['"-"',"{command down}"],
				"Tap West":['"z"',"{command down}"],
				"Tap East":['"z"',"{command down, shift down}"],
				"Tap North":["space","{shift down}"],
				"Tap South":"space",
				"Tap Center":['"r"',"{command down, shift down}"]}
	if action in actions:
		key_press = actions[action]
		
		cmd = ""
		if action == "Tap South" or action == "Left Swipe":
			cmd = """
			osascript -e 'tell application "System Events" to keystroke {} '
			""".format(key_press)
		

		else:
			cmd = """
			osascript -e 'tell application "System Events" to keystroke {} using {}'
			""".format(*key_press)

		os.system(cmd)
		
	else:
		pass
	

 

while (1==1):
    if (arduinoSerialData.inWaiting()>0):
        myData = arduinoSerialData.readline()
        press_key_command(myData)
        


