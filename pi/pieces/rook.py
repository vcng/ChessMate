class Rook:
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

        # check vertically above Rook until not valid space
        # rowu : row up or above Rook
        for rowu in reversed(range(0, r)):
            if chess_board[(rowu, c)] is None:
                valid_locs.append((rowu, c))
            else:
                # check for enemy in next spot if enemy and valid location append to valid_locs
                if chess_board.is_enemy((rowu, c), piece):
                    valid_locs.append((rowu, c))
                break

        # check vertically below Rook until not valid space
        # rowd : row down or below Rook
        for rowd in range(r + 1, 8):
            if chess_board[(rowd, c)] is None:
                valid_locs.append((rowd, c))
            else:
                # check for enemy in next spot if enemy and valid location append to valid_locs
                if chess_board.is_enemy((rowd, c), piece):
                    valid_locs.append((rowd, c))
                break


        # check horizontally right of Rook until not valid space
        # colr : column right of the Rook
        for colr in range(c + 1, 8):
            if chess_board[(r, colr)] is None:
                valid_locs.append((r, colr))
            else:
                # check for enemy in next spot if enemy and valid location append to valid_locs
                if chess_board.is_enemy((r, colr), piece):
                    valid_locs.append((r, colr))
                break


        # check horizontally left of Rook until not valid space
        # coll : column left of the Rook
        for coll in reversed(range(0, c)):
            if chess_board[(r, coll)] is None:
                valid_locs.append((r, coll))
            else:
                # check for enemy in next spot if enemy and valid location append to valid_locs
                if chess_board.is_enemy((r, coll), piece):
                    valid_locs.append((r, coll))
                break

        return valid_locs
