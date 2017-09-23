from util import *


class Knight:
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

        if is_valid_location((r + 2, c + 1)):
            valid_locs.append((r + 2, c + 1))
        if is_valid_location((r + 1, c + 2)):
            valid_locs.append((r + 1, c + 2))
        if is_valid_location((r - 1, c + 2)):
            valid_locs.append((r - 1, c + 2))
        if is_valid_location((r - 2, c + 1)):
            valid_locs.append((r - 2, c + 1))
        if is_valid_location((r - 2, c - 1)):
            valid_locs.append((r - 2, c - 1))
        if is_valid_location((r - 1, c - 2)):
            valid_locs.append((r - 1, c - 2))
        if is_valid_location((r + 1, c - 2)):
            valid_locs.append((r + 1, c - 2))
        if is_valid_location((r + 2, c - 1)):
            valid_locs.append((r + 2, c - 1))

        return valid_locs
