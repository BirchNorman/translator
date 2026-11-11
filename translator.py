import sys
import time
from deep_translator import MyMemoryTranslator

input_path = "/Users/bnorman/Desktop/iCloud Drive (Archive)/Volunteering/St. John's/Needing Translated/input.txt"
output_path = "/Users/bnorman/Desktop/iCloud Drive (Archive)/Volunteering/St. John's/Needing Translated/output.txt"

Translator = MyMemoryTranslator(source='fr-FR', target='en-GB', email="birch.b.norman@gmail.com")

CHARACTER_LIMIT = 300 # below 500-byte limit w/ French characters

blocks = []
trnslblocks = []
block = []

with open(input_path, 'r', encoding='utf-8', errors='replace') as f:
    text = f.read()

words = text.split() # Preserve paragraphs

for word in words:
    if len(' '.join(block)) + 1 + len(word)  > CHARACTER_LIMIT and block:
        blocks.append(' '.join(block))
        block = []
    block.append(word)
if block:
    blocks.append(' '.join(block))

for block in blocks:
    trnslblock = Translator.translate(block) # request error / save progress
    time.sleep(3) # timeout
    if trnslblock == None:
        trnslblocks.append(block) 
    else:
        if "MYMEMORY" in trnslblock:
            print(trnslblock)
            sys.exit()
        else:
            trnslblocks.append(trnslblock) 

if trnslblocks == None:
    print("Nothing was translated.")
else:
    translated = " ".join(trnslblocks)
    with open(output_path, 'w', encoding='utf-8', errors='replace') as f:
        f.write(translated)
    print("Translation complete.")

# 50,000 characters/day = ~20 pages