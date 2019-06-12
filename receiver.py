import binascii
import RPi.GPIO as IO
import time
con=''
t.end=time().time()+8
while time().time()<t.end:
	IO.setmode (IO.BOARD)       
	IO.setup(40,IO.IN)         
	con.append(IO.input(40))                      
	time.sleep(1)                         
	IO.cleanup()                        
	time.sleep(1)
t.end=time().time()+int(binascii.b2a_uu(con))
con=''
while time().time()<t.end:
	IO.setmode (IO.BOARD)       
	IO.setup(40,IO.IN)         
	con.append(IO.input(40))                      
	time.sleep(1)                         
	IO.cleanup()                        
	time.sleep(1)
print(binascii.b2a_uu(con))