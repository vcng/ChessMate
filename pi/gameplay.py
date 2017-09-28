from board import Board


class State:
    """
    The logical states of the game
    """
    GAME_STARTING = 0
    WAITING_FOR_INPUT = 1
    SHOWING_MOVES = 2


class Event:
    """
    The transition event
    """
    START = 0
    PICK_UP = 1
    SET_DOWN = 2


# Game data
chess_board = Board()
active_piece = None
active_location = None
state = State.GAME_STARTING


class StateMachine:
    """
    Game state machine logic
    """

    @staticmethod
    def start_game(_coord):
        global chess_board

        chess_board.reset()
        return State.WAITING_FOR_INPUT

    @staticmethod
    def piece_picked_up(coord):
        global active_piece
        global active_location

        active_piece = chess_board.remove_piece(coord)
        active_location = coord

        return State.SHOWING_MOVES, ['on', active_piece.get_moves(active_location, chess_board)]

    @staticmethod
    def piece_set_down(coord):
        global active_piece
        global active_location

        chess_board.set_piece(coord, active_piece)
        positions = active_piece.get_moves(active_location, chess_board)

        active_piece = None
        active_location = None

        return State.WAITING_FOR_INPUT, ['off', positions]


# Transitions
# (CurrentState, Event) -> NewState, Output
state_machine_mappings = {
    (State.GAME_STARTING, Event.START): StateMachine.start_game,
    (State.GAME_STARTING, Event.PICK_UP): None,
    (State.GAME_STARTING, Event.SET_DOWN): None,

    (State.WAITING_FOR_INPUT, Event.START): None,
    (State.WAITING_FOR_INPUT, Event.PICK_UP): StateMachine.piece_picked_up,
    (State.WAITING_FOR_INPUT, Event.SET_DOWN): StateMachine.piece_set_down,

    (State.SHOWING_MOVES, Event.START): None,
    (State.SHOWING_MOVES, Event.PICK_UP): StateMachine.piece_picked_up,
    (State.SHOWING_MOVES, Event.SET_DOWN): StateMachine.piece_set_down
}


def toggle_piece(coord):
    """
    Event: A piece was lifted or set down at the specified coordinate
    :param coord: A 2-tuple representing the (row, col) coordinate on the board
    :return: An array - The first index is the command, the second is the parameters (Ex: [on, [(1, 1), (2, 3)])
    """
    global chess_board
    global active_piece
    global active_location
    global state

    row, col = coord[0], coord[1]
    assert 0 <= row <= 7 and 0 <= col <= 7

    if chess_board[coord] is not None:
        state, response = state_machine_mappings[(state, Event.PICK_UP)](coord)
    else:
        state, response = state_machine_mappings[(state, Event.SET_DOWN)](coord)

    return response


def start():
    """
    Initialize a new game
    :return: None
    """
    global state

    state = state_machine_mappings[(state, Event.START)](None)

