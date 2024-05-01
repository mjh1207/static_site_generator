import re
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        split_node = []
        text_list = node.text.split(delimiter)
        if len(text_list) % 2 == 0:
            raise Exception("Invalid markdown syntax")
        for i in range(len(text_list)):
            if text_list[i] == "":
                continue
            if i % 2 == 0:
                split_node.append(TextNode(text_list[i], text_type_text))
            else:
                split_node.append(TextNode(text_list[i], text_type))
        new_nodes.extend(split_node)
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)