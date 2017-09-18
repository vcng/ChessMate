from serial import*

class Protocol():

    def __init__(self):

        self.ser = Serial(port='/dev/ttyACM0', baudrate = 9600)

        while True:
            self.ser.write('start')
            if self.ser.available():
                r = self.ser.readline()
                if r == 'go':
                    break

    def listen(self):
        cmd = self.__listener()
        cmd_list = cmd.split(' ')

        cmd = cmd_list[0]

        if cmd == 'go':
            pass
            #do something
        elif cmd == 'tog':
            pass
            #do something, call toggle_piece from game play interface which returns a list

        return

    def __listener(self):
        while True:
            if self.ser.available():
                input = self.ser.readline()
                break
        return input

    def __init_arduino(self):
        #initialize the arduino
        return


    def led_on(self, color, loc):
        #send an led cmd to arduino
        return

    def led_off(self, loc):
        #send a shut off led cmd to arduino
        return





