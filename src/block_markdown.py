import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = list(filter(lambda block: block != '', markdown.split("\n\n")))
    for i in range(len(blocks)):
        blocks[i] = blocks[i].strip(' \n')
        i += 1
    return blocks
        
def block_to_block_type(block):
    if re.match(r"^#{1,6} .*", block):
        return block_type_heading
    elif re.match(r"^```\s(.*)\s```$", block):
        return block_type_code
    elif re.match(r"^>.*|(^> .*|(\s>.*)+)", block):
        return block_type_quote
    elif re.match(r"(^(\*|-) .*|(\n(\*|-) .*))", block):
        return block_type_unordered_list

    ordered_list = False
    block_split = block.split("\n")
    for i in range(len(block_split)):
        if not re.match(fr"^{str(i + 1)}. .*", block_split[i].strip()):
            ordered_list = False
            break
        else:
            ordered_list = True
    if ordered_list == True:
        return block_type_ordered_list
    return block_type_paragraph