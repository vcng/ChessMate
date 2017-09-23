import gameplay
import util

gameplay.start()
moves = []

print('''
--- --- ---
This is a simulation of the hardware, without actually needing the physical chess board.
You will be asked to select the location of a piece to pick up, and where to set that
piece down.

Valid moves will be highlighted on the board, but these are NOT enforced. Feel free to
move pieces around to whatever location you want and take a look at what their valid
moves would be.

To exit, enter -1.
--- --- ---
''')

while True:
    print()
    print(gameplay.chess_board)

    row = 0
    col = 0

    while True:
        try:
            row = int(input('Enter the row (-1 to exit): '))
        except Exception:
            print('Invalid value, try again')
            continue

        if row == -1:
            exit(0)

        try:
            col = int(input('Enter the column (-1 to exit): '))
        except Exception:
            print('Invalid value, try again')
            continue

        if col == -1:
            exit(0)

        if not util.is_valid_location((row, col)) or gameplay.chess_board[(row, col)] is None:
            print('There is no piece at this location. Please try again.\n')
            continue

        moves = gameplay.toggle_piece((row, col))[1]

        print('Possible legal moves:', moves)

        break

    print()
    print(gameplay.chess_board.get_string_representation(moves))
    print('You are holding:', gameplay.active_piece)

    while True:
        try:
            row = int(input('Enter the row (-1 to exit): '))
        except Exception:
            print('Invalid value, try again')
            continue

        if row == -1:
            exit(0)

        try:
            col = int(input('Enter the column (-1 to exit): '))
        except Exception:
            print('Invalid value, try again')
            continue

        if col == -1:
            exit(0)

        if not util.is_valid_location((row, col)) or gameplay.chess_board[(row, col)] is not None:
            print('There is a piece at this location, or the coordinate is out of bounds. Please try again.\n')
            continue

        gameplay.toggle_piece((row, col))

        break

