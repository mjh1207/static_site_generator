from textnode import TextNode, text_node_to_html_node
from htmlnode import HtmlNode
from leafnode import LeafNode
from parentnode import ParentNode
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links
)


def main():
    node = TextNode("This is a text node", "bold")
    print(node.__repr__())
    images = extract_markdown_images("This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)")
    links = extract_markdown_links("This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)")
    no_links = extract_markdown_links("This is some text without any links")
    print(no_links)

main()