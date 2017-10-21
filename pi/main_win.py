# Windows test driver with protocol

import gameplay
from serial import *
from board import *

gameplay.start()

ser = Serial('COM6', 115200)

#gameplay.toggle_piece((1, 4))
gameplay.chess_board.set_piece((5, 2), Piece(PieceType.KING, True)) # 5 2

while True:
    command = ser.readline()
    if not command.strip():
        continue

    print '>', command
    args = command.split(' ')

    if args[0] == 't':
        row = int(args[1])
        col = int(args[2])

        response = gameplay.toggle_piece((row, col))
        if response is not None:
            cmd, args = response
            formatted = ':'.join(str(v[0]) + ':' + str(v[1]) for v in args)
            print 'SENDING', cmd + ':' + str(len(args)) + ':' + formatted + '\n'
            ser.write(cmd + ':' + str(len(args)) + ':' + formatted + '\n')

    print gameplay.chess_board
