from textnode import TextNode, text_node_to_html_node
from htmlnode import HtmlNode
from leafnode import LeafNode
from parentnode import ParentNode


def main():
    node = TextNode("This is a text node", "bold")
    print(node.__repr__())
    parent_node = ParentNode("div", [
        ParentNode("section", [LeafNode("p", "some paragraph")], {"width": "100%"}),
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ], {"class": "my_class"})

    print(parent_node.to_html())
    print(text_node_to_html_node(node).__repr__())

main()