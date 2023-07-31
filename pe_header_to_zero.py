#!/usr/bin/python3 -u

import struct
import shutil
import sys

if len(sys.argv) != 3:
    print("Usage: pe_header_to_zero.py <input_file> <output_file>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

# Copy the original file to a new file
shutil.copy(input_file, output_file)

with open(output_file, "r+b") as f:
    # PE header starts with "MZ". At offset 0x3C, there's a pointer to the PE header start
    f.seek(0x3C, 0)
    pe_offset = struct.unpack('<H', f.read(2))[0]

    # The CheckSum field is at offset 0x58 from the start of the PE header
    f.seek(pe_offset + 0x58, 0)
    f.write(struct.pack('<I', 0))  # Write 0 to CheckSum
