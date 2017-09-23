class Pawn:
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

        if piece.is_black:
            if chess_board[(r + 1, c)] is None:
                valid_locs.append((r + 1, c))
                if chess_board[(r + 2, c)] is None and not piece.moved:
                    valid_locs.append((r + 2, c))

        else:
            if chess_board[(r - 1, c)] is None:
                valid_locs.append((r - 1, c))
                if chess_board[(r - 2, c)] is None and not piece.moved:
                    valid_locs.append((r - 2, c))

        return valid_locs
