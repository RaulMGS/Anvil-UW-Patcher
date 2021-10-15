from os import error
import sys
import Util.FileHandling as filehandler

# 32:9 - 39 8e 63 40
BYTES_32_9 = b"\x39\x8e\x63\x40"
# 21:9 - 9a 99 19 40
BYTES_21_9 = b"\x9a\x99\x19\x40"
# 16:9 - 39 8E E3 3F
BYTES_16_9 = b"#\x39\x8E\xE3\x3F"

# Check if executable file exists
if not filehandler.file_exists(sys.argv[1]):
    print("Invalid input file")
    exit()

# Read original file
byteData = filehandler.file_read_bytes(sys.argv[1])

# Check if the file is in original state
if byteData.find(BYTES_16_9) == -1:
    print("File is already patched or unsupported. Restore backup before patching again")
    exit()

# Save a backup of the original
filehandler.file_write_bytes(sys.argv[1] + ".bak", byteData)

if sys.argv[2] == "21:9":
    print("Patching to 21:9")
    byteData = byteData.replace(BYTES_16_9, BYTES_21_9)
elif sys.argv[2] == "32:9":
    byteData = byteData.replace(BYTES_16_9, BYTES_32_9)
    print("Patching to 32:9")
else:
    print("Invalid aspect ratio format. Valid options: 21:9 | 32:9")

# Write new file
filehandler.file_write_bytes(sys.argv[1], byteData)
print("Successfully patched file")