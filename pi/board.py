class Board:
    """
    The Board data structure
    Represents the state of an 8 x 8 game board, and allows the user to
    set pieces down and take pieces off
    """

    def __init__(self):
        self.board = []
        for _ in range(0, 8):
            self.board.append([None] * 8)

    def remove_piece(self, coord):
        """
        Remove a piece from the board
        :param coord: A 2-tuple representing the (row, col) coordinate on the board
        :return: The removed piece
        """
        piece = self.board[coord[0]][coord[1]]
        self.board[coord[0]][coord[1]] = None
        return piece

    def set_piece(self, coord, piece):
        """
        Set a piece on the board
        There must not be a piece already in the given coordinate
        :param coord: A 2-tuple representing the (row, col) coordinate on the board
        :param piece: The piece to add
        :return: None
        """
        if self.board[coord[0]][coord[1]] is not None:
            raise Exception("Attempted to set piece on coordinate %s, there already exists a piece" % coord)

        self.board[coord[0]][coord[1]] = piece

    def __getitem__(self, coord):
        """
        Get a piece at a given coordinate
        :param coord: A 2-tuple representing the (row, col) coordinate on the board
        :return: The piece at the given coordinate if it exists, otherwise None
        """
        return self.board[coord[0]][coord[1]]

    def __setitem__(self, coord, piece):
        """
        Set a piece on the board, this is equivalent to the method set_piece
        There must not be a piece already in the given coordinate
        :param coord: A 2-tuple representing the (row, col) coordinate on the board
        :param piece: The piece to add
        :return: None
        """
        self.set_piece(coord, piece)
