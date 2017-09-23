from board import Piece, PieceType, Board
from pieces.king import King
from pieces.knight import Knight
from pieces.queen import Queen
from pieces.rook import Rook
from pieces.pawn import Pawn
from pieces.bishop import Bishop

chessB = Board()
chessB.reset()

K = King()
Kn = Knight()
Q = Queen()
R = Rook()

P1 = Piece(PieceType.PAWN, False)   # false == white
P2 = Piece(PieceType.PAWN, True)    # True == Black
P3 = Piece(PieceType.PAWN, False)   # false == white
P4 = Piece(PieceType.PAWN, True)    # True == Black
P1.moved = True                     # cant move twice
P2.moved = True                     # cant move twice

locations = []

# chessB.set_piece((4, 4), Piece(PieceType.QUEEN, False))
# print(Bishop.get_moves((4, 4), None, chessB))
# print(Bishop.get_moves((0, 0), None, chessB))
# print(Bishop.get_moves((7, 7), None, chessB))
# print(Bishop.get_moves((3, 5), None, chessB))

locations = King.get_moves((4, 6), K, chessB)
locations = King.get_moves((5, 5), K, chessB)
locations = King.get_moves((6, 8), K, chessB)

locations = Knight.get_moves((5, 5), Kn, chessB)
locations = Knight.get_moves((3, 4), Kn, chessB)
locations = Knight.get_moves((6, 3), Kn, chessB)

locations = Queen.get_moves((4, 4), Q, chessB)
locations = Queen.get_moves((2, 1), Q, chessB)
locations = Queen.get_moves((7, 7), Q, chessB)

locations = Rook.get_moves((4, 4), Q, chessB)
locations = Rook.get_moves((2, 1), Q, chessB)
locations = Rook.get_moves((7, 7), Q, chessB)

print(Pawn.get_moves((1, 0), P1, chessB))
print(Pawn.get_moves((1, 1), P2, chessB))
print(Pawn.get_moves((1, 2), P3, chessB))
print(Pawn.get_moves((1, 3), P4, chessB))

print(Pawn.get_moves((6, 0), P1, chessB))
print(Pawn.get_moves((1, 1), P2, chessB))
print(Pawn.get_moves((6, 4), P3, chessB))
print(Pawn.get_moves((1, 7), P4, chessB))

print(Pawn.get_moves((6, 0), P4, chessB))
print(Pawn.get_moves((1, 1), P3, chessB))
print(Pawn.get_moves((6, 4), P2, chessB))
print(Pawn.get_moves((1, 7), P1, chessB))

