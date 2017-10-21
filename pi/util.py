def is_valid_location(coord):
    """
    Check if a coordinate is within the range (0, 7) inclusive for each coordinate part
    :param coord: A 2-tuple representing the (row, col) coordinate on the board
    :return: Boolean, True if the coordinate is within range
    """
    row, col = coord[0], coord[1]
    return 0 <= row <= 7 and 0 <= col <= 7

#def detect_check(piece):
    """
    Detects if teams king is in "check" based on the movements on board
    :param piece: a king object
    :return: Boolean, True if king passed in is in check else false
    """
    