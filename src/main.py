from textnode import TextNode, text_node_to_html_node
from htmlnode import HtmlNode
from leafnode import LeafNode
from parentnode import ParentNode
from inline_markdown import split_nodes_delimiter


def main():
    node = TextNode("This is a text node", "bold")
    print(node.__repr__())

    node2 = TextNode("This is text with a `code block` word", "text")
    node3 = TextNode("This is bold text", "bold")
    node4 = TextNode("This is text with *italics*", "text")
    text_nodes = split_nodes_delimiter(split_nodes_delimiter([node2, node3, node4], "`", "code"), "*", "inline")
    print(text_nodes)
    # text_nodes = split_nodes_delimiter(text_nodes, "*", "italic")
    # print(text_nodes)
    

main()