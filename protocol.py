from serial import*

class Protocol():

    def __init__(self):

        self.ser = Serial(port='/dev/ttyACM0', baudrate = 9600)

        while True:
            self.ser.write('start')
            if self.__received():
                break

    def listen(self):
        cmd = self.__listener()
        cmd_list = cmd.split(' ')

        cmd = cmd_list[0]

        if cmd == 'tog':
            return (cmd[1], cmd[2])         #retrun the toggled coord

        return (-2,-2)                      #recieved input not valid, send error code

    def __listener(self):
        while True:
            if self.ser.available():
                input = self.ser.readline()
                break
        return input

    def __received(self):
        for x in range(0,50):
            if self.ser.available():
                input = self.ser.available
                if input == 'go':
                    return True
        return False

    def __received(self, debug):

        return


    def __init_arduino(self):
        #initialize the arduino
        self.ser.write('init')
        if self.__received():
            return True
        return False


    def __led_on(self, loc):
        #send an led cmd to arduino
        self.ser.write('led 1 ' + loc[0] + ' ' + loc[1])    # led 1 r c -> means led 1 = on, r = row, c = col

        #wait for a response
        if self.__received():
            return True
        return False


    def __led_off(self, loc):
        #send a shut off led cmd to arduino
        self.ser.write('led 0 ' + loc[0] + ' ' + loc[1])    # led 0 r c -> means led 0 = off, r = row, c = col

        # wait for a response
        if self.__received():
            return True
        return False

    def invalid_move(self, loc):

        return

    def show_moves(self, *loc):
        for coord in range(0, len(loc)):
            if self.__led_on((coord[0],coord[1])):
                continue
            else:
                return False                #broke along the way try again
        return True                         #leds on, return

    def reset_arduino(self):
        self.ser.write('reset')
        if self.__received():
            self.__init_arduino()
            if self.__received():
                return True
        return False







