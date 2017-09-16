class King:
    @staticmethod
    def get_moves(cord, piece, chess_board):
        valid_locs = []
        r, c = cord[0], cord[1]

        valid_locs.append((r + 1, c))
        valid_locs.append((r + 1, c + 1))
        valid_locs.append((r, c + 1))
        valid_locs.append((r - 1, c + 1))
        valid_locs.append((r - 1, c))
        valid_locs.append((r - 1, c - 1))
        valid_locs.append((r, c - 1))
        valid_locs.append((r + 1, c - 1))

        return valid_locs
