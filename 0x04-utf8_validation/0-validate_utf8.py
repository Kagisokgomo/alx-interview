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
