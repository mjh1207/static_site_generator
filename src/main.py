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
from copy_directory import (
    delete_directory_contents,
    initialize_public_directory
)


def main():
    delete_directory_contents('./public')
    initialize_public_directory()

main()