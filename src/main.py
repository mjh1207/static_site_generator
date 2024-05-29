from textnode import TextNode, text_node_to_html_node
from htmlnode import HtmlNode
from leafnode import LeafNode
from parentnode import ParentNode
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links
)
from block_markdown import (
    markdown_to_blocks,
    block_to_block_type,
    markdown_to_html_node

)


def main():
    node = TextNode("This is a text node", "bold")
    # print(node.__repr__())

    markdown = """```console.log("Hello worldd")```"""
    markdown_blocks = markdown_to_blocks(markdown)
    markdown_to_html_node(markdown)
    

main()