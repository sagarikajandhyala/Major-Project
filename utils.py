# utils.py
# Helper functions for converting text to bits and bits back to text

def text_to_bits(text):
    """
    Convert a string into a list of bits (0/1).
    Each character is represented using 8-bit ASCII.
    """
    bits = []
    for char in text:
        ascii_val = ord(char)              # character -> ASCII
        bin_str = format(ascii_val, '08b') # ASCII -> 8-bit binary string
        bits.extend([int(b) for b in bin_str])
    return bits


def bits_to_text(bits):
    """
    Convert a list of bits (0/1) back into a string.
    Assumes bits length is a multiple of 8.
    """
    chars = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        if len(byte) < 8:
            break
        bin_str = ''.join(str(b) for b in byte)
        ascii_val = int(bin_str, 2)
        chars.append(chr(ascii_val))
    return ''.join(chars)
