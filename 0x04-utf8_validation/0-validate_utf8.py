#!/usr/bin/python3
def validUTF8(data):
    num_bytes = 0  # Number of bytes expected for the current character

    for byte in data:
        # Get the 8 least significant bits (the byte)
        byte = byte & 0xFF
        
        # Determine the number of bytes in the current UTF-8 character
        if num_bytes == 0:
            if (byte >> 7) == 0b0:  # 1-byte character (0xxxxxxx)
                continue
            elif (byte >> 5) == 0b110:  # 2-byte character (110xxxxx)
                num_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character (1110xxxx)
                num_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character (11110xxx)
                num_bytes = 3
            else:
                return False  # Invalid start byte
        else:
            # Expecting continuation bytes (10xxxxxx)
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0  # If we expect no more bytes, it's valid

    """ Determine if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing bytes.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0

    for num in data:
        # Mask to get the first 8 bits
        byte = num & 0xFF

        if num_bytes == 0:
            if (byte >> 7) == 0b0:
                continue  # 1-byte character
            elif (byte >> 5) == 0b110:
                num_bytes = 1  # 2-byte character
            elif (byte >> 4) == 0b1110:
                num_bytes = 2  # 3-byte character
            elif (byte >> 3) == 0b11110:
                num_bytes = 3  # 4-byte character
            else:
                return False  # Invalid leading byte

        else:
            if (byte >> 6) != 0b10:
                return False  # Invalid continuation byte
            num_bytes -= 1

    return num_bytes == 0  # Check if all bytes were used correctly

    num_bytes = 0  # Number of bytes to expect in a valid character

    for num in data:
        # Check the first byte and determine how many bytes are in this character
        if num_bytes == 0:
            if (num >> 7) == 0b0:  # 1-byte character
                continue
            elif (num >> 5) == 0b110:  # 2-byte character
                num_bytes = 1
            elif (num >> 4) == 0b1110:  # 3-byte character
                num_bytes = 2
            elif (num >> 3) == 0b11110:  # 4-byte character
                num_bytes = 3
            else:
                return False  # Invalid UTF-8 start byte

        else:
            # Expect continuation byte
            if (num >> 6) != 0b10:
                return False

        num_bytes -= 1  # Decrease the expected byte count

    return num_bytes == 0  # Ensure all bytes were accounted for
