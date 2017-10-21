from protocol import Protocol
from gameplay import *

if __name__ == "__main__":
    protocol = Protocol(port='COM5', debug=True)
    start()

    while True:
        response = protocol.listen(debug=True)
        if response is 'error':
            exit('Error in protocol')

        print 'GOT RESPONSE #1 "', response, '"'

        response = toggle_piece(response)

        print 'GOT RESPONSE #2 "', response, '"'

        if response is not None:
            protocol.show_moves(response, debug=True)
