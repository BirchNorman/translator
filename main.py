import os
import sys
from txtblocks import *
from docblocks import *

dir_path = "/Users/bnorman/Desktop/iCloud Drive (Archive)/Volunteering/St. John's/Needing Translated"
os.chdir(dir_path)
file_path = input("txt: ") + ".txt"

try:
    with open(file_path, "r", encoding="utf-8") as f:
        text_content = f.read()
except Exception as e:
    print(f"{e}")
    sys.exit()

print(file_path)

txtblocks(file_path)
txtblocks = [f for f in os.listdir()[1:] if f != file_path]
txtblocks.sort()
print(txtblocks)

for num, txtblock in enumerate(txtblocks):
    block_number = num + 1
    docblocks(txtblock, block_number)
    os.remove(txtblock)

docblocks = [f for f in os.listdir()[1:] if f != file_path]
docblocks.sort()
print(docblocks)

# os.remove(file_path)