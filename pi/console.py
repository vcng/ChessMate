import gameplay
import util

gameplay.start()
moves = []

# Initial instructions
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

# Simulation loop
while True:

    # Local variables
    row = 0
    col = 0

    # Print the initial board
    print()
    print(gameplay.chess_board)

    # Keep trying to pick up a piece until a valid instruction is given
    while True:

        # Get the row
        try:
            row = int(input('Enter the row (-1 to exit): '))
        except Exception:
            print('Invalid value, try again')
            continue

        if row == -1:
            exit(0)

        # Get the column
        try:
            col = int(input('Enter the column (-1 to exit): '))
        except Exception:
            print('Invalid value, try again')
            continue

        if col == -1:
            exit(0)

        # Ensure valid location
        if not util.is_valid_location((row, col)) or gameplay.chess_board[(row, col)] is None:
            print('There is no piece at this location. Please try again.\n')
            continue

        # Let gameplay know the piece was picked up
        # It returns the highlighted tiles
        moves = gameplay.toggle_piece((row, col))[1]

        print('Possible legal moves:', moves)

        break

    # Print out the board with the highlighted pieces
    print()
    print(gameplay.chess_board.get_string_representation(moves))
    print('You are holding:', gameplay.active_piece)

    # Keep trying to put down a piece until a valid instruction is given
    while True:

        # Get the row
        try:
            row = int(input('Enter the row (-1 to exit): '))
        except Exception:
            print('Invalid value, try again')
            continue

        if row == -1:
            exit(0)

        # Get the column
        try:
            col = int(input('Enter the column (-1 to exit): '))
        except Exception:
            print('Invalid value, try again')
            continue

        if col == -1:
            exit(0)

        # Ensure valid location
        if not util.is_valid_location((row, col)) or gameplay.chess_board[(row, col)] is not None:
            print('There is a piece at this location, or the coordinate is out of bounds. Please try again.\n')
            continue

        # Let gameplay know the piece is being set down
        gameplay.toggle_piece((row, col))

        break

