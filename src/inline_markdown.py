import re
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
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

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        original_text = node.text
        extracted_images = extract_markdown_images(node.text)
        if extracted_images == []:
            new_nodes.append(TextNode(node.text, text_type_text))
            continue
        for text, url in extracted_images:
            split_text = original_text.split(f"![{text}]({url})", 1)
            if split_text[0] != '':
                new_nodes.append(TextNode(split_text[0], text_type_text))
            new_nodes.append(TextNode(text, text_type_image, url))
            del split_text[0]
            original_text = ''.join(split_text)
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        original_text = node.text
        extracted_links = extract_markdown_links(node.text)
        if extracted_links == []:
            new_nodes.append(TextNode(node.text, text_type_text))
            continue
        for text, url in extracted_links:
            split_text = original_text.split(f"[{text}]({url})", 1)
            if split_text[0] != '':
                new_nodes.append(TextNode(split_text[0], text_type_text))
            new_nodes.append(TextNode(text, text_type_link, url))
            del split_text[0]
            original_text = ''.join(split_text)
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes