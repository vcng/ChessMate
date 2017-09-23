from board import Board


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

        # if piece is black it starts on top and moves down
        if piece.is_black:

            # check locations on board in front of it to make sure its a valid spot to move
            if Board.is_valid_location((r + 1, c)) and chess_board[(r + 1, c)] is None:
                valid_locs.append((r + 1, c))

                # if the piece has not been already moved it can move forward twice
                if Board.is_valid_location((r + 2, c)) and chess_board[(r + 2, c)] is None and not piece.moved:
                    valid_locs.append((r + 2, c))

        # if piece is white it starts on bottom of board and moves up
        else:

            # check locations on board in front of it to make sure its a valid spot to move
            if Board.is_valid_location((r - 1, c)) and chess_board[(r - 1, c)] is None:
                valid_locs.append((r - 1, c))

                # if the piece has not been already moved it can move forward twice
                if Board.is_valid_location((r - 2, c)) and chess_board[(r - 2, c)] is None and not piece.moved:
                    valid_locs.append((r - 2, c))

        return valid_locs
