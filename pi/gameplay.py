from board import Board

chess_board = Board()
active_piece = None
active_location = None


def calculate_highlighting():
    pass


def toggle_piece(coord):
    """
    Event: A piece was lifted or set down at the specified coordinate
    :param coord: A 2-tuple representing the (row, col) coordinate on the board
    :return: None
    """
    global chess_board
    global active_piece
    global active_location

    row, col = coord[0], coord[1]
    if row < 0 or row > 7 or col < 0 or col > 7:
        raise Exception("Coordinate out of bounds (%s, %s)" % coord)

    # If there was already a piece here, this must be a lift event
    if chess_board[coord] is not None:
        if active_piece is None:
            active_piece = chess_board.remove_piece(coord)
            active_location = coord
            calculate_highlighting()
        else:
            raise Exception("Second piece picked up")
    else:
        # Otherwise, this must be a set down event
        # Ensure that there is an active piece
        if active_piece is not None:
            # Set down the active piece at the given location
            chess_board.set_piece(coord, active_piece)
            active_piece = None
            active_location = None
        else:
            raise Exception("Attempted to set down a piece before piece was selected")


def start():
    """
    Initialize a new game
    :return: None
    """
    global chess_board

    chess_board.reset()
