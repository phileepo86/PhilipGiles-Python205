import mosquitto
import serial

portListen = serial.Serial("/dev/cu.usbmodem1421",9600,timeout=2) 
person = mosquitto.Mosquitto("PhilDAT205")
person.connect("127.0.0.1")
#person.subscribe("simon/test")
person.subscribe("ledControl")
   
    

#Writes a method for incoming message
def messageReceived(broker, obj, msg):
    global person
         print("Message " + msg.topic + " containing: " + msg.payload)
        # This switches between ON/OFF serial port
        
        #for msg.payload == "OFF"
              #portListen.Write('0') 
        #for msg.payload == "ON"
              #portListen.Write('1')
        
        
        if msg.payload == "OFF"
             portListen.Write("0")
        
         else: msg.payload == "ON"
                portListen.Write("1")

                
                
                
#Makes the client quit and return
person = None

#Recieve incoming message
person.on_message = messageReceived

#While the client is on - loops
while (person != None): person.loop()