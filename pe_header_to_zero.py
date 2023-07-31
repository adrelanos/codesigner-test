#!/usr/bin/python3 -u

import struct
import shutil

# Copy the original file to a new file
shutil.copy("hello.exe_reattached", "hello.exe_reattached_pe_header_to_zero")

with open("hello.exe_reattached_pe_header_to_zero", "r+b") as f:
    # PE header starts with "MZ". At offset 0x3C, there's a pointer to the PE header start
    f.seek(0x3C, 0)
    pe_offset = struct.unpack('<H', f.read(2))[0]

    # The CheckSum field is at offset 0x58 from the start of the PE header
    f.seek(pe_offset + 0x58, 0)
    f.write(struct.pack('<I', 0))  # Write 0 to CheckSum
