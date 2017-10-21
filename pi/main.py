from protocol import Protocol
from gameplay import *

if __name__ == "__main__":
    protocol = Protocol()

    while True:
        response = protocol.listen()
        if response is 'error':
            exit('Error in protocol')

        response = toggle_piece(response)
        protocol.show_moves(response)
