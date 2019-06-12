import binascii
import RPi.GPIO as IO            
st = "hello world"
con=len(' '.join(format(ord(x), 'b') for x in st))
for x in con:
IO.setmode (IO.BOARD)       
IO.setup(40,IO.OUT)         
IO.output(40,x)                      
time.sleep(1)                         
IO.cleanup()                        
time.sleep(1)        
con=' '.join(format(ord(x), 'b') for x in st)
for x in con:
IO.setmode (IO.BOARD)       
IO.setup(40,IO.OUT)         
IO.output(40,x)                      
time.sleep(1)                         
IO.cleanup()                        
time.sleep(1)          