class Bishop:
    @staticmethod
    def get_moves(cord, piece, chess_board):
        valid_locs = []
        r, c = cord[0], cord[1]

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
