class PieceType:
    """
    Enum representing all the different types of pieces
    """

    KING = 0
    QUEEN = 1
    ROOK = 2
    KNIGHT = 3
    BISHOP = 4
    PAWN = 5


class Piece:
    """
    Represents the state of a piece on a Board
    """

    def __init__(self, piece_type, is_black):
        """
        Init
        :param piece_type: The type of piece, should be one of PieceType
        :param is_black: True if the piece is black, False if the piece is white
        """
        self.piece_type = piece_type
        self.is_black = is_black
        self.moved = False

    def get_moves(self, coord, chess_board):
        return {
            PieceType.KING: None,
            PieceType.QUEEN: None,
            PieceType.ROOK: None,
            PieceType.KNIGHT: None,
            PieceType.BISHOP: None,
            PieceType.PAWN: None
        }[self.piece_type](coord, self, chess_board)

    def __str__(self):
        """
        String conversion override
        :return: String representation of the piece
        """
        symbol = {
            PieceType.KING: 'K',
            PieceType.QUEEN: 'Q',
            PieceType.ROOK: 'R',
            PieceType.KNIGHT: 'H',
            PieceType.BISHOP: 'B',
            PieceType.PAWN: 'P'
        }[self.piece_type] or '?'

        if not self.is_black:
            symbol = symbol.lower()

        return symbol


def create_starting_layout():
    """
    Create a new starting board layout with all pieces in their correct
    starting positions
    :return: A 2d array of pieces
    """
    return [
        [
            Piece(PieceType.ROOK, False), Piece(PieceType.KNIGHT, False), Piece(PieceType.BISHOP, False),
            Piece(PieceType.KING, False), Piece(PieceType.QUEEN, False), Piece(PieceType.BISHOP, False),
            Piece(PieceType.KNIGHT, False), Piece(PieceType.ROOK, False)
        ],
        [
            Piece(PieceType.PAWN, False), Piece(PieceType.PAWN, False), Piece(PieceType.PAWN, False),
            Piece(PieceType.PAWN, False), Piece(PieceType.PAWN, False), Piece(PieceType.PAWN, False),
            Piece(PieceType.PAWN, False), Piece(PieceType.PAWN, False)
        ],
        [None] * 8,
        [None] * 8,
        [None] * 8,
        [None] * 8,
        [
            Piece(PieceType.PAWN, True), Piece(PieceType.PAWN, True), Piece(PieceType.PAWN, True),
            Piece(PieceType.PAWN, True), Piece(PieceType.PAWN, True), Piece(PieceType.PAWN, True),
            Piece(PieceType.PAWN, True), Piece(PieceType.PAWN, True)
        ],
        [
            Piece(PieceType.ROOK, True), Piece(PieceType.KNIGHT, True), Piece(PieceType.BISHOP, True),
            Piece(PieceType.KING, True), Piece(PieceType.QUEEN, True), Piece(PieceType.BISHOP, True),
            Piece(PieceType.KNIGHT, True), Piece(PieceType.ROOK, True)
        ],
    ]


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

    def reset(self):
        """
        Reset the board to a valid starting state
        :return: None
        """
        self.board = create_starting_layout()

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

    def __str__(self):
        """
        String conversion override
        :return: String representation of the board
        """
        output = ""
        for row in self.board:
            output += ' | '.join([str(piece or ' ') for piece in row]) + "\n"
        return output
