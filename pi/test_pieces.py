import unittest
import board

from pieces.king import King
from pieces.knight import Knight
from pieces.queen import Queen
from pieces.rook import Rook
from pieces.pawn import Pawn
from pieces.bishop import Bishop


class TestPieces(unittest.TestCase):

    def test_pawn(self):
        b = board.Board()

        b.set_piece((1, 1), board.Piece(board.PieceType.PAWN, True))
        b.set_piece((6, 1), board.Piece(board.PieceType.PAWN, False))

        self.assertItemsEqual([
            (2, 1),
            (3, 1)
        ], Pawn.get_moves((1, 1), b[(1, 1)], b))
        self.assertItemsEqual([
            (5, 1),
            (4, 1)
        ], Pawn.get_moves((6, 1), b[(6, 1)], b))

    def test_king(self):
        b = board.Board()

        b.set_piece((1, 1), board.Piece(board.PieceType.KING, True))

        self.assertItemsEqual([
            (0, 0),
            (0, 1),
            (0, 2),
            (1, 0),
            (1, 2),
            (2, 0),
            (2, 1),
            (2, 2)
        ], King.get_moves((1, 1), b[(1, 1)], b))

    def test_knight(self):
        b = board.Board()

        b.set_piece((1, 1), board.Piece(board.PieceType.KNIGHT, True))

        self.assertItemsEqual([
            (3, 2),
            (2, 3),
            (0, 3),
            (3, 0)
        ], Knight.get_moves((1, 1), b[(1, 1)], b))

    def test_bishop(self):
        b = board.Board()

        b.set_piece((1, 1), board.Piece(board.PieceType.BISHOP, True))

        self.assertItemsEqual([
            (0, 0),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (0, 2),
            (2, 0)
        ], Bishop.get_moves((1, 1), b[(1, 1)], b))

    def test_rook(self):
        b = board.Board()

        b.set_piece((1, 1), board.Piece(board.PieceType.ROOK, True))

        self.assertItemsEqual([
            (0, 1),
            (2, 1),
            (3, 1),
            (4, 1),
            (5, 1),
            (6, 1),
            (7, 1),
            (1, 0),
            (1, 2),
            (1, 3),
            (1, 4),
            (1, 5),
            (1, 6),
            (1, 7)
        ], Rook.get_moves((1, 1), b[(1, 1)], b))

    def test_queen(self):
        b = board.Board()

        b.set_piece((1, 1), board.Piece(board.PieceType.QUEEN, True))

        self.assertItemsEqual([
            (0, 1),
            (2, 1),
            (3, 1),
            (4, 1),
            (5, 1),
            (6, 1),
            (7, 1),
            (1, 0),
            (1, 2),
            (1, 3),
            (1, 4),
            (1, 5),
            (1, 6),
            (1, 7),
            (0, 0),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (0, 2),
            (2, 0)
        ], Queen.get_moves((1, 1), b[(1, 1)], b))


if __name__ == "__main__":
    unittest.main()
