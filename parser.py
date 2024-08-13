def parse_ascii(bytes):
    result_string = ''

    for byte in bytes:
        if byte < 128:
            result_string += chr(byte)
        else:
            return 'Non-ASCII string'
    
    return result_string