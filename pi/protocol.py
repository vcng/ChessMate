# Programmer: Miles Avelli
# Date: 9/24/2017

from serial import*
import time

class Protocol():

    def __init__(self, s, debug = None):
        """ Constructor for Protocol class, sets up port for USB Serial.
        :param s: Is for starting serial.
        :param debug: If debug is set, prints debug statements.
        """

        self.ser = s

        found = False

        # Check if in debug mode
        if debug is None:

            # Check ports 0-9 for Arduino
            for port in range(0,10):
                try:
                    self.ser = Serial('/dev/ttyAcm%s' % port, 115200)    # Creates Serial instance
                    if self.ser:    # If serial was created
                        found = True    # Found the port
                        break
                except Exception:
                    pass

            # Runs if port is found
            if found:
                # Loop until synced with Arduino
                while True:
                    self.ser.flushInput()   # Clear serial input buffer
                    self.ser.write('start') # Send 'start' to Arduino
                    if self.__received():   # Wait for response
                        break
            else:
                return

        # Debug mode
        else:
            print '== initializing serial port =='

            for port in range(0,10):
                print '== trying port ' + str(port) + ' ==',
                try:
                    self.ser = Serial('/dev/ttyACM%s' % port, 115200)
                    if self.ser:
                        print'== port found =='
                        found = True
                        break
                except Exception:
                    print '$$ error could not find port $$'
                    pass

            if found:
                print '== syncing with arduino =='
                while True:
                    self.ser.flushInput()
                    self.ser.write('start')
                    print '== writing start =='
                    if self.__received(1):
                        print'== sync complete =='
                        break
            else:
                print '$$ error could not initialize $$'
                return


    def listen(self, debug = None):
        """ listen is used to poll the serial port until the Arduino sends a command and
        then returns a list with the command or an error.
        :param debug:   If debug is set, prints debug statements.
        :return:        Returns a list, either a toggle command list or an error.
        """

        # Check if in debug mode
        if debug is None:
            cmd = self.__listener()     # Call __listener to get the command from Arduino
            cmd_list = cmd.split(' ')   # Make the received string into a list of strings split on spaces

            cmd = cmd_list[0]           # Make cmd the first element of cmd_list, which is the cmd name

            if cmd == 't':              # t = toggle
                return [cmd, cmd_list[1], cmd_list[2].replace("\r\n","")]   # Returns the toggled coord
            else:
                return ['error']    # Received input not valid, send error code

        # Debug mode
        else:
            print '== starting listener =='
            cmd = self.__listener()
            cmd_list = cmd.split(' ')

            print '== received command ' + str(cmd_list[0]) + ' =='
            cmd = cmd_list[0]
            print '== buffer size: ' + str(self.ser.inWaiting()) + ' =='
            if cmd == 't':
                print '== returning toggle coord =='
                return [cmd, cmd_list[1], str(cmd_list[2]).replace("\r\n","")]
            else:
                print'$$ error command not found $$'
                return ['error']


    def __listener(self, debug = None):
        """ Helper used to retrieve serial input from Arduino, polls the serial buffer until input is detected.
        :param debug:   If debug is set, prints debug statements.
        :return:        Returns a string that was read from the Arduino over serial port.
        """

        # Check if in debug mode
        if debug is None:
            while True:
                if self.ser.inWaiting() > 0:    # If there is something in the serial input buffer
                    input = self.ser.readline() # Read the serial input buffer
                    break
            return input

        # Debug mode
        else:
            print '== listening ==',
            while True:
                if self.ser.inWaiting() > 0:
                    print '== incoming =='
                    input = self.ser.readline()
                    break
            print '== read ' + input + ' =='
            return input

    def __received(self, debug = None):
        """
        Used for polling the Arduino for confirmation of input
        :param debug:   If debug is set, prints debug statements
        :return:        Returns True for confirmed input, or False if something broke
        """

        # Check if in debug mode
        if debug is None:
            # Check the buffer 10 times.
            for x in range(0,10):
                if self.ser.inWaiting() > 0:
                    input = self.ser.readline()
                    if input[0] == 'g' and input[1] == 'o': # Checks the input for 'go' command
                        return True
                time.sleep(1) # Pause for 1 second between checks

        # Debug mode
        else:
            print '== waiting .',
            for x in range(0,10):
                print '.',
                if self.ser.inWaiting() > 0:
                    print '== got a response =='
                    print '== buffer size: ',
                    print self.ser.inWaiting(),
                    print ' =='
                    input = self.ser.readline()
                    print input
                    if input[0] == 'g' and input[1] == 'o':
                        print '== received go =='
                        return True
                time.sleep(1)
            print '$$ error __received $$'
        return False


    def __init_arduino(self, debug = None):
        """ Sends the initialize command to the Arduino.
        :param debug: If debug is set, prints debug statements.
        :return:      True for successful initialization, False for failed attempt.
        """

        # Check if in debug mode
        if debug is None:
            self.ser.write('i')             # i = init, sends to Arduino
            if self.__received():           # Call __received function, which waits for Arduino to confirm input
                return True
            return False

        #Debug mode
        else:
            print '== sending init call to arduino =='
            self.ser.write('i')
            if self.__received(1):
                print '== arduino ready =='
                return True
            print '$$ error __init_arduino $$'
            return False

    def __led_on(self, loc, debug = None):
        """ Sends an led on command to the Arduino in the form: 'l 1 r c'.
        l = led command name
        1 = led on
        r = row
        c = column
        :param loc:     Location of the change in the form of a tuple, where [0] is r and [1] is c.
        :param debug:   If debug is set, then print debug statements.
        :return:        Returns True for confirmed input, or False if something broke.
        """

        # Check if in debug mode
        if debug is None:
            # Send an led command to arduino
            self.ser.write('l 1 ' + str(loc[0]) + ' ' + str(loc[1]))

            # Wait for a response
            if self.__received():
                return True
            return False

        # Debug mode
        else:
            print '== led on command =='
            print '== sending ' + str(loc[0]) + ' ' + str(loc[1]) + ' =='
            self.ser.write('l 1 ' + str(loc[0]) + ' ' + str(loc[1]))
            # wait for a response
            if self.__received(1):
                return True
            print '$$ error __led_on $$'
            return False


    def __led_off(self, loc, debug = None):
        """ Sends an led on command to the Arduino in the form: 'l 0 r c'.
        l = led command name
        0 = led off
        r = row
        c = column
        :param loc:     Location of the change in the form of a tuple, where [0] is r and [1] is c.
        :param debug:   If debug is set, then print debug statements.
        :return:        Returns True for confirmed input, or False if something broke.
        """

        # Check if in debug mode
        if debug is None:
            # Send an led cmd to arduino
            self.ser.write('l 0 ' + str(loc[0]) + ' ' + str(loc[1]))

            # Wait for a response
            if self.__received():
                return True
            return False

        # Debug mode
        else:
            print '== led off command =='
            print '== sending ' + str(loc[0]) + str(loc[1]) + ' =='
            self.ser.write('l 0 ' + str(loc[0]) + ' ' + str(loc[1]))
            if self.__received(1):
                return True
            print '$$ error __led_off $$'
            return False

    ## Not defined yet
    def invalid_move(self, loc, debug = None):

        return

    def light_moves(self, loc, debug = None):
        """ Used to send led commands to the Arduino from the driver. Since this takes in a list
        it can be handle multiple coordinates at the same time.
        :param loc: Location of the change in the form of a list, index 0 is led on or off followed by the
        coordinates r and c for the change.
        :param debug:   If debug is set, print debug statements.
        :return:        Returns True for confirmed input, or False if something broke.
        """

        # Check if in debug mode
        if debug is None:
            # If on command, use __led_on
            if loc[0] == 'on':
                loc.pop(0)      # Delete front element, resulting in a list of coordinates only

                # Iterate over the coordinates in loc, sending them to __led_on to send a command to Arduino
                for x in range(0, len(loc)):
                    if self.__led_on(([loc[x][0],loc[x][1]])):
                        continue
                    else:
                        return False                # Broke along the way try again
                return True                         # Led's on, return

            # Else use __led_off
            else:
                loc.pop(0)
                for x in range(0,len(loc)):
                    if self.__led_off(([loc[x][0], loc[x][1]])):
                        continue
                    else:
                        return False
                return True

        # Debug mode
        else:
            if loc[0] == 'on':
                loc.pop(0)
                print '== show moves command =='
                print '== sending locations' + loc + ' =='
                for x in range(0, len(loc)):
                    if self.__led_on(([loc[x][0],loc[x][1]]),1):
                        continue
                    else:
                        print '$$ error show_moves $$'
                        return False                # broke along the way try again
                print '== all locations sent =='
                return True
            else:
                loc.pop(0)
                print '== hide moves command =='
                print '== sending locations ' + loc + ' =='
                for x in range(0,len(loc)):
                    if self.__led_off(([loc[x][0], loc[x][1]]),1):
                        continue
                    else:
                        print '$$ error hide_moves $$'
                        return False  # broke along the way try again
                print '== all locations sent =='
                return True

    def reset_arduino(self, debug = None):
        """ Sends the reset command to the Arduino.
        :param debug:   If debug is set, print debug statements.
        :return:        Returns True for confirmed input, or False if something broke.
        """

        # Check if in debug mode
        if debug is None:
            self.ser.write('r')             # r = reset
            if self.__received():           # Wait for response
                if self.__init_arduino():   # Call __init_arduino to initialize the Arduino
                    return True
            return False

        # Debug mode
        else:
            print '== resetting arduino =='
            print '== sending reset command =='
            self.ser.write('r')
            if self.__received(1):
                print '== reset received, initializing sync with arduino'
                if self.__init_arduino(1):
                    print '== reset complete =='
                    return True
            print '$$ error reset_arduino $$'
            return False
