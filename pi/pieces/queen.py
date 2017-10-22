class Queen:
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

        # check vertically above queen until not valid space
        # rowu : row up or above queen
        for rowu in reversed(range(0, r)):
            if chess_board[(rowu, c)] is None:
                valid_locs.append((rowu, c))
            else:
                # check for enemy in next spot if enemy and valid location append to valid_locs
                if chess_board.is_enemy((rowu, c), piece):
                    valid_locs.append((rowu, c))
                break

        # check vertically below queen until not valid space
        # rowd : row down or below queen
        for rowd in range(r + 1, 8):
            if chess_board[(rowd, c)] is None:
                valid_locs.append((rowd, c))
            else:
                # check for enemy in next spot if enemy and valid location append to valid_locs
                if chess_board.is_enemy((rowd, c), piece):
                    valid_locs.append((rowd, c))
                break

        # check horizontally right of queen until not valid space
        # colr : column right of the queen
        for colr in range(c + 1, 8):
            if chess_board[(r, colr)] is None:
                valid_locs.append((r, colr))
            else:
                # check for enemy in next spot if enemy and valid location append to valid_locs
                if chess_board.is_enemy((r, colr), piece):
                    valid_locs.append((r, colr))
                break

        # check horizontally left of queen until not valid space
        # coll : column left of the queen
        for coll in reversed(range(0, c)):
            if chess_board[(r, coll)] is None:
                valid_locs.append((r, coll))
            else:
                # check for enemy in next spot if enemy and valid location append to valid_locs
                if chess_board.is_enemy((r, coll), piece):
                    valid_locs.append((r, coll))
                break

        # Loop to add spaces below and to the right of the bishop
        for off in range(1, 8):
            new_r = r + off
            new_c = c + off

            # if the offset pushes the piece off the board brake out
            if new_r > 7 or new_c > 7 or new_r < 0 or new_c < 0:
                break
            # if the chessboard holds None (no other piece) then add right and down direction
            if chess_board[(new_r, new_c)] is None:
                valid_locs.append((new_r, new_c))
            else:
                # append location if enemy can be captured
                if chess_board.is_enemy((new_r, new_c), piece):
                    valid_locs.append((new_r, new_c))
                break

        # Loop to add spaces below and to the left of the bishop
        for off in range(1, 8):
            new_r = r - off
            new_c = c + off

            # if the offset pushes the piece off the board brake out
            if new_r > 7 or new_c > 7 or new_r < 0 or new_c < 0:
                break

            # if the chessboard holds None (no other piece) then add left and down direction
            if chess_board[(new_r, new_c)] is None:
                valid_locs.append((new_r, new_c))
            else:
                # append location if enemy can be captured
                if chess_board.is_enemy( (new_r, new_c), piece):
                    valid_locs.append((new_r, new_c))
                break

        # Loop to add spaces above and to the right of the bishop
        for off in range(1, 8):
            new_r = r + off
            new_c = c - off

            # if the offset pushes the piece off the board brake out
            if new_r > 7 or new_c > 7 or new_r < 0 or new_c < 0:
                break
            # if the chessboard holds None (no other piece) then add right and up direction
            if chess_board[(new_r, new_c)] is None:
                valid_locs.append((new_r, new_c))
            else:
                # append location if enemy can be captured
                if chess_board.is_enemy((new_r, new_c), piece):
                    valid_locs.append((new_r, new_c))
                break

        # Loop to add spaces above and to the left of the bishop
        for off in range(1, 8):
            new_r = r - off
            new_c = c - off

            # if the offset pushes the piece off the board brake out
            if new_r > 7 or new_c > 7 or new_r < 0 or new_c < 0:
                break

            # if the chessboard holds None (no other piece) then add left and up direction
            if chess_board[(new_r, new_c)] is None:
                valid_locs.append((new_r, new_c))
            else:
                # append location if enemy can be captured
                if chess_board.is_enemy( (new_r, new_c), piece):
                    valid_locs.append((new_r, new_c))
                break

        return valid_locs
