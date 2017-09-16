class Rook:
    @staticmethod
    def get_moves(cord, piece, chess_board):
        valid_locs = []
        r, c = cord[0], cord[1]

        # check vertically above Rook until not valid space
        # rowu : row up or above Rook
        for rowu in reversed(range(0, r)):
            if chess_board[(rowu, c)] is None:
                valid_locs.append((rowu, c))
            else:
                break

        # check vertically below Rook until not valid space
        # rowd : row down or below Rook
        for rowd in range(r + 1, 8):
            if chess_board[(rowd, c)] is None:
                valid_locs.append((rowd, c))
            else:
                break

        # check horizontally right of Rook until not valid space
        # colr : column right of the Rook
        for colr in range(c + 1, 8):
            if chess_board[(r, colr)] is None:
                valid_locs.append((r, colr))
            else:
                break

        # check horizontally left of Rook until not valid space
        # coll : column left of the Rook
        for coll in reversed(range(0, c)):
            if chess_board[(r, coll)] is None:
                valid_locs.append((r, coll))
            else:
                break

        return valid_locs
