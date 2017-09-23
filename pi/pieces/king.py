from board import Board


class King:
    @staticmethod
    def get_moves(cord, piece, chess_board):
        """
        :param cord:            row and column of piece on board
        :param piece:           instance of the piece's object class
        :param chess_board:     the chessboard the pieces are on
        :return:
        """
        valid_locs = []
        r, c = cord[0], cord[1]

        # down
        if Board.is_valid_location((r + 1, c)):
            valid_locs.append((r + 1, c))

        # right down
        if Board.is_valid_location((r + 1, c + 1)):
            valid_locs.append((r + 1, c + 1))

        # right
        if Board.is_valid_location((r, c + 1)):
            valid_locs.append((r, c + 1))

        # right up
        if Board.is_valid_location((r - 1, c + 1)):
            valid_locs.append((r - 1, c + 1))

        # up
        if Board.is_valid_location((r - 1, c)):
            valid_locs.append((r - 1, c))

        # left up
        if Board.is_valid_location((r - 1, c - 1)):
            valid_locs.append((r - 1, c - 1))

        # left
        if Board.is_valid_location((r, c - 1)):
            valid_locs.append((r, c - 1))

        # left down
        if Board.is_valid_location((r + 1, c - 1)):
            valid_locs.append((r + 1, c - 1))

        return valid_locs
