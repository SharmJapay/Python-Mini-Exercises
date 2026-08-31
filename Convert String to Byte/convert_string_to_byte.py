"""Different ways on how to convert a number to a string"""

import struct


def main():
    """Start the program and run all steps in order."""

    # Case 1: Primary Methods (Recommended)
    my_string = "Hello 🐍"

    # Method 1: Use of .encode() method

    # Uses default utf-8 encoding
    bytes_data1 = my_string.encode()

    print(bytes_data1)
    # Output: b'Hello \xf0\x9f\x90\x8d'

    # Explicitly specifying encoding
    bytes_data_ascii = my_string.encode("ascii", errors="ignore")

    print(bytes_data_ascii)
    # Output: b'Hello '

    # Method 2: Use of bytes() Constructor
    bytes_data2 = bytes(my_string, encoding="utf-8")

    print(bytes_data2)
    # Output: b'Hello \xf0\x9f\x90\x8d'

    # Method 3: Use of bytearray() Constructor
    mutable_bytes = bytearray(my_string, encoding="utf-8")

    mutable_bytes[0] = 104  # Changes 'H' to 'h'
    print(mutable_bytes)
    # Output: bytearray(b'hello \xf0\x9f\x90\x8d')

    # Case 2: Handling Hexadecimal and Escape Strings
    hex_string = "48656c6c6f"
    escaped_str = "\\x00\\x01\\x41"

    # Method 1: Use of bytes.fromhex() (For Hex Strings)
    bytes_data3 = bytes.fromhex(hex_string)

    print(bytes_data3)
    # Output: b'Hello'

    # Method 2: Use of raw_unicode_escape (For Raw Escape Sequences)
    bytes_data4 = bytes(escaped_str, encoding="raw_unicode_escape")

    print(bytes_data4)
    # Output: b'\x00\x01A'

    # Case 3: Specialized & Alternative Approaches

    my_string1 = "Hello"

    # Method 1: Mapping Unicode Ordinals (ord)
    bytes_data = bytes(map(ord, my_string1))

    print(bytes_data)
    # Output: b'Hello'

    # Method 2: Use of struct.pack()
    my_string2 = "Hello".encode("utf-8")

    # Packs the string into an exact byte format
    packed_bytes = struct.pack(f"{len(my_string2)}s", my_string2)

    print(packed_bytes)
    # Output: b'Hello'


if __name__ == "__main__":
    main()
