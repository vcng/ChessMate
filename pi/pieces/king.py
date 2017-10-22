from util import *


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
        if is_valid_location((r + 1, c)) and (chess_board[(r + 1, c)] is None
                or chess_board.is_enemy((r + 1, c), piece)):
            valid_locs.append((r + 1, c))

        # right down
        if is_valid_location((r + 1, c + 1)) and (chess_board[(r + 1, c + 1)] is None
                or chess_board.is_enemy((r + 1, c + 1), piece)):
            valid_locs.append((r + 1, c + 1))

        # right
        if is_valid_location((r, c + 1)) and (chess_board[(r, c + 1)] is None
                or chess_board.is_enemy((r, c + 1), piece)):
            valid_locs.append((r, c + 1))

        # right up
        if is_valid_location((r - 1, c + 1)) and (chess_board[(r - 1, c + 1)] is None
                or chess_board.is_enemy((r - 1, c + 1), piece)):
            valid_locs.append((r - 1, c + 1))

        # up
        if is_valid_location((r - 1, c)) and (chess_board[(r - 1, c)] is None
                or chess_board.is_enemy((r - 1, c), piece)):
            valid_locs.append((r - 1, c))

        # left up
        if is_valid_location((r - 1, c - 1)) and (chess_board[(r - 1, c - 1)] is None
                or chess_board.is_enemy((r - 1, c - 1), piece)):
            valid_locs.append((r - 1, c - 1))

        # left
        if is_valid_location((r, c - 1)) and (chess_board[(r, c - 1)] is None
                or chess_board.is_enemy((r, c - 1), piece)):
            valid_locs.append((r, c - 1))

        # left down
        if is_valid_location((r + 1, c - 1)) and (chess_board[(r + 1, c - 1)] is None
                or chess_board.is_enemy((r + 1, c - 1), piece)):
            valid_locs.append((r + 1, c - 1))

        return valid_locs
