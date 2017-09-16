class Queen:
    @staticmethod
    def get_moves(cord, piece, chess_board):
        valid_locs = []
        r, c = cord[0], cord[1]

        # check vertically above queen until not valid space
        # rowu : row up or above queen
        for rowu in reversed(range(0, r)):
            if chess_board[(rowu, c)] is None:
                valid_locs.append((rowu, c))
            else:
                break

        # check vertically below queen until not valid space
        # rowd : row down or below queen
        for rowd in range(r + 1, 8):
            if chess_board[(rowd, c)] is None:
                valid_locs.append((rowd, c))
            else:
                break

        # check horizontally right of queen until not valid space
        # colr : column right of the queen
        for colr in range(c + 1, 8):
            if chess_board[(r, colr)] is None:
                valid_locs.append((r, colr))
            else:
                break

        # check horizontally left of queen until not valid space
        # coll : column left of the queen
        for coll in reversed(range(0, c)):
            if chess_board[(r, coll)] is None:
                valid_locs.append((r, coll))
            else:
                break

        for off in range(1, 8):
            new_r = r + off
            new_c = c + off

            if new_r > 7 or new_c > 7 or new_r < 0 or new_c < 0:
                break

            if chess_board[(new_r, new_c)] is None:
                valid_locs.append((new_r, new_c))
            else:
                break

        for off in range(1, 8):
            new_r = r - off
            new_c = c + off

            if new_r > 7 or new_c > 7 or new_r < 0 or new_c < 0:
                break

            if chess_board[(new_r, new_c)] is None:
                valid_locs.append((new_r, new_c))
            else:
                break

        for off in range(1, 8):
            new_r = r + off
            new_c = c - off

            if new_r > 7 or new_c > 7 or new_r < 0 or new_c < 0:
                break

            if chess_board[(new_r, new_c)] is None:
                valid_locs.append((new_r, new_c))
            else:
                break

        for off in range(1, 8):
            new_r = r - off
            new_c = c - off

            if new_r > 7 or new_c > 7 or new_r < 0 or new_c < 0:
                break

            if chess_board[(new_r, new_c)] is None:
                valid_locs.append((new_r, new_c))
            else:
                break

        return valid_locs
