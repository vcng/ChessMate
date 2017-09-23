from board import Board


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

        # down down right
        if Board.is_valid_location((r + 2, c + 1)):
            valid_locs.append((r + 2, c + 1))

        # down right right
        if Board.is_valid_location((r + 1, c + 2)):
            valid_locs.append((r + 1, c + 2))

        # up right right
        if Board.is_valid_location((r - 1, c + 2)):
            valid_locs.append((r - 1, c + 2))

        # up up right
        if Board.is_valid_location((r - 2, c + 1)):
            valid_locs.append((r - 2, c + 1))

        # down down left
        if Board.is_valid_location((r - 2, c - 1)):
            valid_locs.append((r - 2, c - 1))

        # up left left
        if Board.is_valid_location((r - 1, c - 2)):
            valid_locs.append((r - 1, c - 2))

        # down left left
        if Board.is_valid_location((r + 1, c - 2)):
            valid_locs.append((r + 1, c - 2))

        # down down left
        if Board.is_valid_location((r + 2, c - 1)):
            valid_locs.append((r + 2, c - 1))

        return valid_locs
