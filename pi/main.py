# Windows test driver with protocol

import gameplay
from serial import *

gameplay.start()

ser = Serial('COM6', 9600)

while True:
    command = ser.readline()
    if not command.strip():
        continue

    print '>', command
    args = command.split(' ')

    if args[0] == 't':
        cmd, args = gameplay.toggle_piece((int(args[1]), int(args[2])))
        formatted = ':'.join(str(v[0]) + ':' + str(v[1]) for v in args)
        ser.write(cmd + ':' + str(len(args)) + ':' + formatted + '\n')

    print gameplay.chess_board
