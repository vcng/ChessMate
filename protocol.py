from serial import*

class Protocol():

    def __init__(self, debug = None):
        found = False
        if debug is None:
            for port in range(0,10):
                try:
                    self.ser = Serial('/dev/ttyAcm%s' %port, 9600)
                    if self.ser:
                        found = True
                        break
                except Exception:
                    pass

            if found:
                while True:
                    self.ser.write('start')
                    if self.__received():
                        break
            else:
                return
        else:
            print('== initializing serial port ==')

            for port in range(0,10):
                print('== trying port',port,'==', sep = ' ')
                try:
                    self.ser = Serial('/dev/ttyACM%s' %port, 9600)
                    if self.ser:
                        print('== port found ==')
                        found = True
                        break
                except Exception:
                    print('$$ error could not find port $$')
                    pass

            if found:
                print('== syncing with arduino ==')
                while True:
                    self.ser.write('start')
                    if self.__received(1):
                        print('== sync complete ==')
                        break
            else:
                print('$$ error could not initialize $$')
                return

    def listen(self, debug = None):
        if debug is None:
            cmd = self.__listener()
            cmd_list = cmd.split(' ')

            cmd = cmd_list[0]

            if cmd == 'tog':
                return ['tog',cmd[1], cmd[2]]         #retrun the toggled coord

            return ['error']                      #recieved input not valid, send error code

        #debug mode
        else:
            print('== starting listener ==')
            cmd = self.__listener()
            cmd_list = cmd.split(' ')

            print('== received command ' + str(cmd_list[0]) + ' ==')
            cmd = cmd_list[0]

            if cmd == 'tog':
                print('== returning toggle coord ==')
                return ['tog', cmd[1], cmd[2]]  # return the toggled coord

            print('$$ error command not found $$')
            return ['error']

    def __listener(self, debug = None):
        if debug is None:
            while True:
                if self.ser.available():
                    input = self.ser.readline()
                    break
            return input
        else:
            print('== listening.', end = '')
            count = 0
            while True:
                if count < 10:
                    print('.', end = '')
                else:
                    count = 0
                    print('.')
                if self.ser.available():
                    print('== incoming ==')
                    input = self.ser.readline()
                    break
            print('== read',input,'==')
            return input

    def __received(self, debug = None):
        if debug is None:
            for x in range(0,50):
                if self.ser.available():
                    input = self.ser.available
                    if input == 'go':
                        return True
        else:
            print('== waiting .', end = '')
            for x in range(0,50):
                print('.', end = '')
                if self.ser.available():
                    input = self.ser.available
                    if input == 'go':
                        print('== received go ==')
                        return True
            print('$$ error __received $$')
        return False


    def __init_arduino(self, debug = None):
        #initialize the arduino
        if debug is None:
            self.ser.write('init')
            if self.__received():
                return True
            return False
        else:
            print('== sending init call to arduino ==')
            self.ser.write('init')
            if self.__received(1):
                print('== arduino ready ==')
                return True
            print('$$ error __init_arduino $$')
            return False

    def __led_on(self, loc, debug = None):
        if debug is None:
            #send an led cmd to arduino
            self.ser.write('led 1 ' + str(loc[0]) + ' ' + str(loc[1]))    # led 1 r c -> means led 1 = on, r = row, c = col

            #wait for a response
            if self.__received():
                return True
            return False
        else:
            print('== led on command ==')
            print('== sending', str(loc[0]), str(loc[1]), '==', sep=' ')
            self.ser.write('led 1 ' + str(loc[0]) + ' ' + str(loc[1]))  # led 1 r c -> means led 1 = on, r = row, c = col
            # wait for a response
            if self.__received(1):
                return True
            print('$$ error __led_on $$')
            return False


    def __led_off(self, loc, debug = None):
        if debug is None:
            #send an led cmd to arduino
            self.ser.write('led 0 ' + str(loc[0]) + ' ' + str(loc[1]))    # led 1 r c -> means led 1 = on, r = row, c = col

            #wait for a response
            if self.__received():
                return True
            return False
        else:
            print('== led off command ==')
            print('== sending',str(loc[0]),str(loc[1]),'==', sep = ' ')
            self.ser.write('led 0 ' + str(loc[0]) + ' ' + str(loc[1]))  # led 1 r c -> means led 1 = on, r = row, c = col
            # wait for a response
            if self.__received(1):
                return True
            print('$$ error __led_off $$')
            return False

    def invalid_move(self, loc, debug = None):

        return

    def show_moves(self, *loc, debug = None):
        if debug is None:
            for x in range(0, len(loc)):
                if self.__led_on([loc[x][0],loc[x][1]]):
                    continue
                else:
                    return False                #broke along the way try again
            return True                         #leds on, return
        else:
            print('== show moves command ==')
            print('== sending locations',loc,'==', sep = ' ')

            for x in range(0, len(loc)):
                if self.__led_on([loc[x][0],loc[x][1]]):
                    continue
                else:
                    print('$$ error show_moves $$')
                    return False                #broke along the way try again
            print('== all locations sent ==')
            return True

    def hide_moves(self, *loc, debug = None):
        if debug is None:
            for x in range(0, len(loc)):
                if self.__led_off([loc[x][0],loc[x][1]]):
                    continue
                else:
                    return False                #broke along the way try again
            return True                         #leds on, return
        else:
            print('== hide moves command ==')
            print('== sending locations',loc,'==', sep = ' ')

            for x in range(0, len(loc)):
                if self.__led_off([loc[x][0],loc[x][1]]):
                    continue
                else:
                    print('$$ error hide_moves $$')
                    return False                #broke along the way try again
            print('== all locations sent ==')
            return True


    def reset_arduino(self, debug = None):
        if debug is None:
            self.ser.write('reset')
            if self.__received():
                self.__init_arduino()
                if self.__received():
                    return True
            return False
        else:
            print('== resetting arduino ==')
            print('== sending reset command ==')
            self.ser.write('reset')
            if self.__received(1):
                print('== reset received, initializing sync with arduino')
                self.__init_arduino(1)
                if self.__received(1):
                    print('== reset complete ==')
                    return True
            print('$$ error reset_arduino $$')
            return False







