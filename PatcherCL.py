import sys
import Util.FileHandling as filehandler

# 32:9 - 39 8e 63 40
BYTES_32_9 = b"\x39\x8e\x63\x40"
# 21:9 - 9a 99 19 40
BYTES_21_9 = b"\x9a\x99\x19\x40"
# 16:9 - 39 8E E3 3F
BYTES_16_9 = b"#\x39\x8E\xE3\x3F"

# Read original file
byteData = filehandler.file_read_bytes(sys.argv[1])

# Save a backup of the original
filehandler.file_write_bytes( sys.argv[1] + ".bak",byteData)

# Patches default cutscene aspect ratio to 21:9 aspect ratio
if sys.argv[2] == "21:9":
    print("Patching to 21:9")
    byteData = byteData.replace(BYTES_16_9, BYTES_21_9)
    
# Patches default cutscene aspect ratio to 32:9 aspect ratio
elif sys.argv[2] == "32:9":
    byteData = byteData.replace(BYTES_16_9, BYTES_32_9)
    print("Patching to 32:9")

else: 
    print("Invalid aspect ratio format")

# Write new file
filehandler.file_write_bytes(sys.argv[1], byteData)