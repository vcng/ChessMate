import gameplay
import util

gameplay.start()
moves = []

while True:
    print()
    print(gameplay.chess_board)

    row = 0
    col = 0

    while True:
        try:
            row = int(input('Enter the row: '))
        except Exception:
            print('Invalid value, try again')
            continue

        try:
            col = int(input('Enter the column: '))
        except Exception:
            print('Invalid value, try again')
            continue

        if not util.is_valid_location((row, col)) or gameplay.chess_board[(row, col)] is None:
            print('There is no piece at this location. Please try again.')
            continue

        moves = gameplay.toggle_piece((row, col))[1]

        print('Possible legal moves:', moves)

        break

    print()
    print(gameplay.chess_board.get_string_representation(moves))

    while True:
        try:
            row = int(input('Enter the row: '))
        except Exception:
            print('Invalid value, try again')
            continue

        try:
            col = int(input('Enter the column: '))
        except Exception:
            print('Invalid value, try again')
            continue

        if not util.is_valid_location((row, col)) or gameplay.chess_board[(row, col)] is not None:
            print('There is a piece at this location, or the coordinate is out of bounds. Please try again.')
            continue

        gameplay.toggle_piece((row, col))

        break

