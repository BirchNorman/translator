def txtblocks(file_path: str):

    CHARACTER_LIMIT = 3500

    current_block = []
    current_length = 0
    block_number = 1

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if current_length + len(line) > CHARACTER_LIMIT and current_block:
                with open(f'block{block_number}.txt', 'w', encoding='utf-8') as f:
                    f.write(' '.join(current_block))

                    current_block = []
                    current_length = 0
                    block_number += 1

            current_block.append(line)
            current_length += len(line)

    if current_block:
        with open(f'block{block_number}.txt', 'w', encoding='utf-8') as f:
            f.write(' '.join(current_block))