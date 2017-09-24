# Programmer: Miles Avelli
# Date: 9/24/2017

from protocol import Protocol
import time

p = Protocol(1,1)   # Create a Protocol instance in debug mode

input = ""  # used for reading input

# Test loop for listening to Arduino
while True:

    # Every 10th iteration, call reset_arduino
    for x in range(0,10):
        input = p.listen(1)     # Listen for Arduino commands in debug mode
        if input[0] == 't':     # If received a toggle command
            print input         # Print the input
            #call toggle piece
            time.sleep(0.1)     # Delay
        else:
            print 'jargon'      # Otherwise something else was read, print error
            time.sleep(0.1)     # Delay
        if x == 9:
            if p.reset_arduino(1):
                continue
            else:
                time.sleep(3600)# If reset breaks, delay for 1 hour for debugging results.
