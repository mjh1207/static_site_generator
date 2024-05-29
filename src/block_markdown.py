import re

from parentnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

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

def markdown_to_html_node(markdown):
    children =[]
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        children.append(block_to_html_node(block))
    return ParentNode("div", children, None)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
        return block_to_paragraph(block)
    elif block_type == block_type_heading:
        return block_to_heading(block)
    elif block_type == block_type_code:
        return block_to_code(block)
    elif block_type == block_type_quote:
        return block_to_quote(block)
    elif block_type == block_type_unordered_list:
        return block_to_unordered_list(block)
    elif block_type == block_type_ordered_list:
        return block_to_ordered_list(block)
    else:
        raise Exception("Invalid block type")
    
def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for node in text_nodes:
        children.append(text_node_to_html_node(node))
    return children

def block_to_paragraph(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def block_to_heading(block):
    level = 0
    for letter in block:
        if letter == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def block_to_code(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError(f"Invalid code block")
    text = block[4 : -3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])

def block_to_quote(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    text = " ".join(new_lines)
    children = text_to_children(text)
    return ParentNode("blockquote", children)

def block_to_unordered_list(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def block_to_ordered_list(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)